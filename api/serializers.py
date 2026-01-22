from rest_framework import serializers
from lisa.models import Product, Order, OrderItem

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
