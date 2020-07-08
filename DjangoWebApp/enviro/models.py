import uuid
from django.db import models
from django.contrib.auth.models import (
		BaseUserManager, AbstractBaseUser
	)

class CategoryManager(models.Manager):
    def create_category(self, category_name):
        category = self.create(category_name=category_name)
        category.save(using=self._db)
        # do something with the book
        return category

class QuantityManager(models.Manager):
    def create_quantity(self, measure, weight):
        quantity = self.create(measure=measure, weight=weight)
        # do something with the book
        return quantity

class ProductManager(models.Manager):
    def create_product(self, product_name, category_id, brand_name, min_order, max_order, quantity_id):
        product =  self.create(
            product_name=product_name, 
            brand_name=brand_name,
            category_id =category_id,
            min_order=min_order,
            max_order=max_order,
            quantity_id=quantity_id
            )
        return product

class UserManager(BaseUserManager):
    def create_user(self, username, password, first_name, last_name, dob, position):
        user = self.create(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            position=position
        )
        return user

class UsageManager(models.Manager):
    def create_usage(self, product_id, date_usage, user_id):
        usage = self.create(
            product_id=product_id,
            date_usage=date_usage,
            user_id=user_id
        )
        return usage

class SupplierManager(models.Manager):
    def create_usage(self, supplier_name):
         supplier = self.create( supplier_name=supplier_name)
         return supplier

class OrderManager(models.Manager):
    def create_order(self, date, supplier_id, user_id):
        order = self.create(date=date,supplier_id=supplier_id,user_id=user_id)
        return order



class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length = 20)
    objects = CategoryManager()

class Quantity (models.Model):
    qunatity_id = models.AutoField(primary_key=True)
    measure = models.CharField(max_length = 15)
    weight = models.IntegerField()
    objects = QuantityManager()

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length= 50)
    brand_name = models.CharField(max_length = 20)
    min_order = models.IntegerField()
    max_order = models.IntegerField()
    quantity_id = models.ForeignKey(Quantity, on_delete=models.SET_NULL, null=True)
    objects = ProductManager()

class User (AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 15, unique = True)
    password = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    dob = models.DateTimeField()
    position = models.CharField(max_length = 25)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)	
    objects = UserManager()

class Usage (models.Model):
    usage_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_usage = models.DateTimeField(auto_now = True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    objects = UsageManager()

class Supplier (models.Model):
    supplier_id = models.AutoField(primary_key = True)
    supplier_name = models.CharField(max_length = 30)
    objects = SupplierManager()

class Order (models.Model):
    order_id = models.AutoField(primary_key = True)
    date = models.DateTimeField(auto_now_add = True)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    objects = OrderManager()
