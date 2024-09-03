from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product
from . models import Order
from . models import CartItem

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',  'price', 'image','image2','image3','describtion']

class OrderForm(forms.ModelForm):
    class Meta:
        model=CartItem
        fields = ['quantity', 'product']
