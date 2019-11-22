from django.shortcuts import render
from .models import Product, Category, Customer, Cart
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import HttpResponse


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html' , {'product':products})

def single(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shop/single-product.html', { 'product': product } )

@login_required
def cart(request, product_id):
    cart = Cart()
    cart.product = get_object_or_404(Product, pk=product_id)
    cart.customer = request.session.get['email']
    cart.save()
    return render(request, 'shop/cart.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            if request.POST['name'] and request.POST['email'] and request.POST['password1']:
                customer = Customer()
                customer.email = request.POST['email']
                customer.name = request.POST['name']
                customer.password = request.POST['password1']
                customer.save()
                return redirect(home)
            else:
                return render(request,'shop/register.html' , {'error' : 'Please fill all the data to submit the form'})
        else:
            return render(request,'shop/register.html' , {'error' : 'Please password was wrong'})
    else:
        return render(request,'shop/register.html')

def login(request):
    if request.method =='POST':
        user = auth.authenticate(username = request.POST['email'], password= request.POST['password1'])
        if user is not None:
            auth.login(request, Customer)
            return redirect(home)
        else:
            return render(request ,'shop/login.html', {'error':'Username and Password is incorrect'})
    else:
        return render(request ,'shop/login.html')

def logout(request):
        auth.logout(request)
        return redirect('home')

def logout(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie createed")
        return render(home)
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response
