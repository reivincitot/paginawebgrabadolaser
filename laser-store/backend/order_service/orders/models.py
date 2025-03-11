from django.db import models


class Order(models.Model):
    user_id = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='pending')
    
    def __str__(self):
        return f'Order {self.id} by User {self.user_id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Item {self.product_id} in Order {self.order.id}'
        