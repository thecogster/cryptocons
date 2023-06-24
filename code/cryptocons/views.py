from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import time
import urllib.parse
import hashlib
import hmac
import base64
import json

# import requests

# Create your views here.
from .models import *

post = [{'loan_title':'Youre Fucked','name': 'roger'},{'loan_title':'Youre Not Fucked','name': 'Mary'}]

def home(request):

    template = 'cryptocons/homepage.html'
    return render(request, template)



# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = authenticate(request, email=email, password=password)
	
#         if user is not None:
#             login(request, user)
#             # Redirect the user to the desired page after successful login
#             return redirect('homepage_url')
#         else:
#             # Authentication failed, display an error message
#             messages.error(request, 'Invalid email or password')

#    return render(request, 'cryptocons/login.html')

@login_required(login_url='login_url')
def craicLounge(request):

	
	return render(request, 'cryptocons/craic_lounge.html')


def register(request):
	# form = UserCreationForm()
	# # if request.user.is_authenticated:
	# # 	return redirect('display')
	# else:
	# 	form = CreateUserForm()

		if request.method == 'POST':
			form = UserRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, f'Account was created for {username}! You can now log in')

				return redirect('login_url')

				
		else:
			form = UserRegisterForm()
				
		return render(request, 'cryptocons/register.html', {'form':form}) 


# 		context = {'form':form}
# 		return render(request, 'accounts/register.html', context)

@login_required(login_url='login_url')
def logoutUser(request):
	logout(request)
	return redirect('/')


def qr_generator(request):
    template = 'cryptocons/qr_generator.html'
    

    return render(request, template)

def qr_scan(request):
    template = 'cryptocons/qr_scan.html'
    
	
    return render(request, template)


# @login_required(login_url='login_url')
def leaderboard(request):
    # Retrieve all users and sort by date joined
    all_users = User.objects.order_by('date_joined')

	## Its a dictionary passed as users to html 
    return render(request, 'cryptocons/leaderboard.html', {'users': all_users})




@login_required(login_url='login_url')
def profile(request):
	from django.shortcuts import render
	from django.contrib.auth.decorators import login_required
	from django.contrib.auth.models import User
	from cryptocons.models import Cards

	current_user = request.user
	cards = Cards.objects.filter(owner=current_user)
	card_count = cards.count()
    # Retrieve the current user's profile information
	profile_info = {
	'username': current_user.username,
	'email': current_user.email,
	'date_joined': current_user.date_joined,
	'last_login': current_user.last_login,
	'card_count': card_count
	}
	context = {'profile_info':profile_info,'cards':cards}
	

	return render(request, 'cryptocons/profile.html', context)
	# return JsonResponse(ticker_details_json, safe=False)
