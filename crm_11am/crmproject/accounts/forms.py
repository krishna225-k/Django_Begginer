from django import forms
from .models import Customers, Products, Orders
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
