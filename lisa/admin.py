from django.contrib import admin
from .models import Product, Order, OrderItem, Action

admin.site.register([Product, Order, OrderItem, Action])