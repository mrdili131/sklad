from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('selling/',views.SellView.as_view(),name='selling'),
    path('products/',views.ProductsView.as_view(),name='products'),
    path('product/<int:id>/',views.ProductView.as_view(),name='product'),
    path('report/',views.ReportView.as_view(),name='report'),
]