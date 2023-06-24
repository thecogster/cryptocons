from contextlib import nullcontext
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Cards
from django import forms
from django.forms import ModelForm, CharField, TextInput

class CardsForm(forms.ModelForm):
    leprechaun_number = forms.CharField( widget=TextInput(attrs={'type':'number'}))
    tier = forms.CharField( widget=TextInput(attrs={'type':'number'}))
    position = forms.CharField( widget=TextInput(attrs={'type':'number'}))
    quantity = forms.CharField( widget=TextInput(attrs={'type':'number'}))

    class Meta:
        model = Cards 
        fields = ['leprechaun_number', 'tier', 'position']


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




