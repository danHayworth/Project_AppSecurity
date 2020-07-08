from django.contrib import admin

from .models import Product, Category, Quantity, User, Usage, Supplier, Order, Supplier

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Quantity)
admin.site.register(Usage)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Supplier)