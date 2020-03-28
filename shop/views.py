from django.shortcuts import render
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.views.generic.list import ListView

from .models import Product, Category, Cart, Customer
from .forms import NameForm


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html' , {'product':products})

def blog(request):
    return render(request, 'shop/blog.html')
    messages.add_messages(request, messages.INFO, 'Hello World.')

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
            import pdb
            pdb.set_trace()
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

class count(ListView):
    model = Product
    template_name = 'shop/count.html'
    context_object_name = 'count_data'

    def get_queryset(self):
        cusomer_list = Customer.objects.all()
        for customer_name in cusomer_list:
            # queryset = {'cusomer_list':Customer.objects.all(),'product_count':Product.objects.filter(cat_id=customer_name.id)}
            # return queryset
            product_count = Product.objects.filter(cat_id=customer_name.id)
            cus_name = customer_name
            queryset = {'product_count':product_count,'cus_name':cus_name}
    
            return queryset