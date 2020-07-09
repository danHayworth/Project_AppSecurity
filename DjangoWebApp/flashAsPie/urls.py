from django.urls import path

from .views import home, order, products, employee

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('order/', order, name='order'),
    path('employee/', employee, name='employee')
]