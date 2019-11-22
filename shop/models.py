from django.db import models
from django.contrib.auth.models import User
from django import forms

class Category(models.Model):
    name = models.CharField(max_length=255)

# Create your models here.
class Product(models.Model):
        cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        description = models.TextField(max_length=12000)
        price = models.IntegerField(default=1)
        photo = models.ImageField(upload_to='images/')
        date = models.DateField(auto_now_add=True)

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=10)

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)
