from django.urls import path

from .views import home, order, products

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('order/', order, name='order')
]