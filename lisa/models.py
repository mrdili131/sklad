from django.db import models
from users.models import User, Filial
import uuid

p_type = [
    ('kilo','kilo'),
    ('dona','dona'),
    ('litr','litr'),
    ('metr','metr')
]

class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    quantity = models.FloatField(default=1)
    p_type = models.CharField(choices=p_type,default='dona',max_length=50)
    comment = models.TextField(null=True,blank=True)
    is_available = models.BooleanField(default=True)
    filial = models.ForeignKey(Filial,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.name}] [{self.quantity} ta] [{self.price} so\'m dan har biri]'
    

class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sold_orders')
    filial = models.ForeignKey(Filial,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    sold_price = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.uuid)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    sold_price = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='order_items')
    filial = models.ForeignKey(Filial,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
