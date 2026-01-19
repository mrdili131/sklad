from django.db import models
from users.models import User, Filial
import uuid

class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    comment = models.TextField(null=True,blank=True)
    is_available = models.BooleanField(default=True)
    filial = models.ForeignKey(Filial,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.name}] [{self.quantity} ta] [{self.price} so\'m dan har biri]'
    

class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sold_items')
    filial = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.uuid)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="orders")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    filial = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
