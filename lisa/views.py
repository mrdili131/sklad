from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Order, OrderItem
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin,View):
    def get(self,request):
        form = ProductForm()
        return render(request,'index.html',{"form":form})
    
    def post(self,request):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.filial = request.user.filial
            product.save()
            return redirect('home')
        return render(request,'index.html',{"form":form})
    

class SellView(LoginRequiredMixin,View):
    def get(self,request):
        products = Product.objects.filter(filial=request.user.filial,is_available=True)
        return render(request,'selling.html',{"products":products})
    
class ProductsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'products.html')
    
class ProductView(LoginRequiredMixin,View):
    def get(self,request,id):
        product = Product.objects.get(id=id)
        form = ProductForm(instance=product)
        return render(request,'edit_product.html',{"product":product,"form":form})
    
    def post(self,request,id):
        product = Product.objects.get(id=id)
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product',id=id)
        return render(request,'edit_product.html',{"product":product,"form":form})