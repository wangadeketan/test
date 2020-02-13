from django.shortcuts import render
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import HttpResponse

from .models import Product, Category, Cart
from .forms import NameForm


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
        customer = NameForm(request.POST)
        if customer.is_valid():
            customer.save()
            return redirect(home)
        else:
            return HttpResponse("Form is Not Valid")
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
