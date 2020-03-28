from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='index'),
     path('<int:product_id>', views.single, name='single'),
     path('<int:product_id>', views.cart, name='cart'),
     path('signup/', views.signup, name='signup'),
     path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),
     path('blog/', views.blog, name='blog'),
     path('count/', views.count.as_view(), name='count'),
]
