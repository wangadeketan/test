from django.contrib import admin
from . models import Category, Product, Customer, OrderItem, Order, Cart

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Cart)