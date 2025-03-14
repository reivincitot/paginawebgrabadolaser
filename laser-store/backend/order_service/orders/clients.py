import requests
from django.conf import settings
from rest_framework.exceptions import APIException
from requests.exceptions import RequestException
import logging

logger = logging.getLogger(__name__)

class ProductServiceClient:
    def __init__(self):
        self.base_url = settings.PRODUCT_SERVICE_URL
        self.timeout = settings.SERVICE_TIMEOUT
        self.auth_token = settings.SERVICE_AUTH_TOKEN
        
    def get_product_stock(self, product_id):
        try:
            response = requests.get(
                f"{self.base_url}/api/products/{product_id}/stock/",
                headers={'Authorization': f'Bearer {self.auth_token}'},
                timeout=self.timeout,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            logger.error(f'Product service error: {str(e)}')
            raise APIException("Error retrieving product information")
        except requests.exceptions.Timeout:
            logger.erro("Product service timeout")
            raise APIException('Product service unavailable')
        except requests.exceptions.RequestException as e:
            logger.error(f"Product service connection error: {str(e)}")
            raise APIException("Error connecting to product service")
        
product_client = ProductServiceClient()