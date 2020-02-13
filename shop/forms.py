''' Copyright: © 2020 Ketan Wangade'''
from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name',max_length=255)
    email = forms.CharField(label='Email',max_length=255)
    password = forms.CharField(label='Password ',max_length=255)