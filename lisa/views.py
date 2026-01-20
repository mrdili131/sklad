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