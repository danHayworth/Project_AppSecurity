from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product, User


@login_required
def home(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }

    return render(request, "home.html", context)

def products(request):
    return render(request, "products.html", {})

@login_required
def order(request):
    return render(request, "order.html", {})


@login_required
def employee(request, user_id):
    employee = User.objects.all()
    return render(request, "employee.html", {})