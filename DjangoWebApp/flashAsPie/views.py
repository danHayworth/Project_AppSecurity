from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Product, User, Order



def home(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }

    return render(request, "home.html", context)



def order(request):
    orders = Order.objects.all()
    context = {
        "orders": orders
    }

    return render(request, "order.html", context)


@login_required
def employee(request, user_id):
    employee = get_object_or_404(User, pk=user_id)
    context = {
        'employee' : employee
    }
    return render(request, "employee.html", context)
