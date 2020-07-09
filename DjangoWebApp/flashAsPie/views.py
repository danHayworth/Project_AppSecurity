from django.shortcuts import render
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Product


@login_required
def home(request):
    products = Product.objects.all()

    context = {
        'products' : products
    }

    return render(request, "home.html", context)

def products(request, product_id):
    return render(request, "products.html", {})


def order(request):
    return render(request, "order.html", {})