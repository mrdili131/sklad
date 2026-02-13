from django.shortcuts import render
from .serializers import ProductsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from lisa.models import Product, Order, OrderItem
from .cart import Cart

class ProductsAPI(APIView):
    def get(self,request):
        products = Product.objects.filter(filial=request.user.filial, is_available=True).order_by("-id")
        serializer = ProductsSerializer(products,many=True)
        return Response(serializer.data)
    
class ProductDetailAPI(APIView):
    def get_object(self,id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return None
        
    def get(self,request,id):
        product = self.get_object(id)
        if not product:
            return Response({"msg":"Could not find the product","status":False})
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
    
    def delete(self,request,id):
        product = self.get_object(id)
        if not product:
            return Response({"msg":"Could not find the product","status":False})
        product.quantity = 0
        product.is_available = False
        product.save()
        return Response({"msg":"Deleted successfully"})
    

class CartAPI(APIView):
    def get(self,request):
        cart = Cart(request).cart
        return Response(cart)
    
    def post(self,request):
        cart = Cart(request)
        product_id = int(request.data.get("product_id"))
        quantity = int(request.data.get("quantity"))
        selling_price = float(request.data.get("selling_price"))
        if (product_id and quantity and selling_price):
            cart.add(product_id,quantity,selling_price)
            return Response(cart.cart)
        else:
            return Response({"msg":"Error adding product into cart","status":False})
        
    def delete(self,request):
        cart = Cart(request)
        product_id = str(request.data.get("product_id"))
        cart.remove(product_id)
        print(product_id)
        return Response({"msg":"Cart is clean now","status":True})
    
class ToOrderAPI(APIView):
    def get(self,request):
        cart = Cart(request)
        if len(cart.cart) == 0:
            return Response({"msg":"Select items first","status":False})
        cart.order()
        return Response({"msg":"Success","status":True})
    
class OrdersListAPI(APIView):
    def get(self,request):
        data = {}
        orders = Order.objects.filter()
        # for order in orders:
            # for i in order.items.all():
        return Response({"status":True})