from django.urls import path
from . import views

urlpatterns = [
    path('single', views.upload_single_file, name='single'),
    path('multiple', views.upload_multiple_file, name='multiple'),
    path('zip', views.upload_zip_file, name='zip'),
]