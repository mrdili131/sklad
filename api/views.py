from django.shortcuts import render
from .serializers import ProductsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from lisa.models import Product

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
        product.delete()
        return Response({"msg":"Deleted successfully"})