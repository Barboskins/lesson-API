from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField()


class ProductOrders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey("Order",on_delete=models.CASCADE, related_name='order_positions')
    quantity = models.PositiveIntegerField()



class Order(models.Model):
    name = models.TextField()
    products = models.ManyToManyField(Product, through=ProductOrders)
    created_at = models.DateTimeField(
        auto_now_add=True
    )