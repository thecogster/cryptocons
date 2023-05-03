from contextlib import nullcontext
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from .models import Business, BusinessLoan

# from .models import Order


# class OrderForm(ModelForm):
# 	class Meta:
# 		model = Order
# 		fields = '__all__'


## inherit from the UserCreationForm
class UserRegisterForm(UserCreationForm):
	email  = forms.EmailField()
	full_name = forms.CharField(max_length=100)
	telephone_number = forms.IntegerField()

	class Meta:
		model = User 
		fields = ['username', 'email', 'full_name', 'telephone_number','password1', 'password2' ]

class UserChangeFormCustom(UserChangeForm):
	class Meta:
		model = User 
		fields = ['username', 'email']


class BusinessApplication(forms.ModelForm):

	class Meta:
		model = Business
		fields = ['business_name', 'business_address', 'company_number', 'business_sector_name']

class LoanApplication(forms.ModelForm):

	class Meta:
		model = BusinessLoan
		fields = ['loan_value', 'currency', 'loan_length_in_days']

