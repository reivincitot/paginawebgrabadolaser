import logging
from celery import shared_task
from celery.exceptions import MaxRetriesExceededError
from django.conf import settings
from django.utils import timezone
from .clients import product_client

logger = logging.getLogger(__name__)

@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=30,
    retry_jitter=True,
    max_retries=3,
    queue='inventory',
    routing_key='inventory.update'
)
def update_inventory_async(self, product_ids, user_id=None):
    """
    Updates the inventory asynchronously after an order.
    Args:
        product_ids (list): List of affected product IDs
        user_id (int): ID of the user performing the operation (optional)
    """
    try:
        logger.info(f'Starting inventory update for {len(product_ids)} products')
        
        # Obtain persisten connection
        with product_client.get_persistent_session() as session:
            for product_id in product_ids:
                try:
                    response = session.post(
                        f'{settings.PRODUCT_SERVICE_URL}/api/products/{product_id}/update-stock',
                        json={'operation': 'decrement', 'quantity':1},
                        headers={'X-Request_ID': str(self.request.id)}
                    )
                    response.raise_for_status()
                    
                    logger.debug(f"Stock updated for product {product_id}")
                    
                except Exception as e:
                    logger.error(f"Error updating stock for product {product_id}: {str(e)}")
                    raise # Triggers retry of the entire task
            
            logger.info("Inventory update completed Successfully")
            return{
                'status': 'success',
                'timestamp': timezone.now().isoformat(),
                'affected_products': len(product_ids)
            }
            
    except Exception as e:
        logger.critical(f"Critical failure in inventory update: {str(e)}")
        self.retry(exc=e, countdown=60)
        
    finally:
        if hasattr(self, 'retries') and self.retries == self.max_retries:
            logger.error("Maximum retries exceeded for inventory update")
            # Compensation or notification logic would go here
            return {
                'status': 'error',
                'message': 'Max retries exceeded',
                'failed_products': product_ids
            }