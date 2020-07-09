from django.contrib import admin
from .models import Product, Category, Quantity, User, Supplier, Order, Supplier

class ProductAdmin (admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'brand_name', 'category', 'units','quantity')
    list_display_links = ('product_id', 'product_name')
    list_filter = ('brand_name', 'category')
    search_fields = ('product_name', 'brand_name')
    list_per_page = 25

class UserAdmin (admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'position', 'is_admin', 'is_staff')
    list_display_links = ('user_id', 'first_name', 'last_name', 'position')
    list_filter = ('position',)
    search_fields = ('first_name', 'last_name', 'position')
    list_per_page = 25

    # list_editable = ('field') - in case we want editable boolean

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Quantity)
admin.site.register(User, UserAdmin)
admin.site.register(Order)
admin.site.register(Supplier)

#dan added a comment
