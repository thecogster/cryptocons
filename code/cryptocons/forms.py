from contextlib import nullcontext
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, CharField, TextInput
import random
from django.db import models
import random
from django.db import models
from cryptocons.models import CardsModel
from .models import Announcement

def generate_random_number():
    return random.randint(1000000, 9999999)

class CardsForm(forms.ModelForm):
    leprechaun_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}))
    tier = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}))
    position = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}))

    class Meta:
        model = CardsModel
        fields = ['leprechaun_number', 'tier', 'position', 'quantity']


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


from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'body']


