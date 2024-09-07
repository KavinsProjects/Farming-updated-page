from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm

class FarmerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['contact_info','address']

class BuyerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['contact_info', 'address']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity','price', 'discount_price', 'category', 'product_type', 'image']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = []

'''
class CustomerForm(ModelForm):
    class Mete:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
'''
class CreateUserForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=Profile.USER_TYPE_CHOICES,required=True,label="Register as")
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2','user_type']

    def save(self, commit = True):
        user = super().save(commit=False)
        user.save()
        profile = Profile.objects.create(user=user, user_type=self.cleaned_data['user_type'])
        return user


