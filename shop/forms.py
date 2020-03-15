''' Copyright: © 2020 Ketan Wangade'''
from django import forms
from .models import Customer
from django.forms import ModelForm

class NameForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['name', 'email', 'password']