from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "home.html", {})

def products(request):
    return render(request, "products.html", {})


def order(request):
    return render(request, "order.html", {})