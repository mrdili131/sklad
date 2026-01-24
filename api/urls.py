from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('products/',views.ProductsAPI.as_view()),
    path('product/<int:id>/',views.ProductDetailAPI.as_view()),
    path('cart/',views.CartAPI.as_view()),
    path('order/',views.ToOrderAPI.as_view()),
]