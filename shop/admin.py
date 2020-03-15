from django.contrib import admin
from . models import Category, Product, Customer, OrderItem, Order, Cart

# Register your models here.

class ProductModelAdmin(admin.ModelAdmin):
	"""Product Model class in a admin"""
	list_display = ["name","price","date"]
	list_display_links = ("price","date")
	#list_filter = ("name")
	class Meta:
		model = Product

admin.site.register(Category)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Cart)