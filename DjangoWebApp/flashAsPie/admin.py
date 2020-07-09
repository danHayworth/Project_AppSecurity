from django.contrib import admin
from flashAsPie.models import Product, Category, Quantity, User, Usage, Supplier, Order, Supplier

class ProductAdmin (admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'brand_name', 'category', 'units','quantity')
    list_display_links = ('product_id', 'product_name')
    list_filter = ('brand_name', 'category')
    search_fields = ('product_name', 'brand_name')
    list_per_page = 25

    # list_editable = ('field') - in case we want editable boolean

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Quantity)
admin.site.register(Usage)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Supplier)

#dan added a comment
