from django.urls import path

from .views import home, order, employee

urlpatterns = [
    path('', home, name='home'),
    path('order/', order, name='order'),
    path('<int:user_id>', employee, name='employee')
]