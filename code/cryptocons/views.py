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




# def home(request):
# 	## Takes list of posts 
# 	## passes the key posts as the access to the lsit of dicts

# 	context = {'businesses': Business.objects.all()}

# 	## render passes request, the directory to the appname/template.html as django auto searches for templates, passes context as the 
# 	## dictionary of posts

# 	return render(request, 'accounts/home.html', context=context)
def home(request):

    template = 'cryptocons/homepage.html'
    return render(request, template)

def craicLounge(request):

	
	return render(request, 'cryptocons/craic_lounge.html')

@login_required(login_url='login_url')
def loanTest(request):
	## Takes list of posts 
	## passes the key posts as the access to the lsit of dicts
	# if request.method =='POST' and 'form1' in request.POST:

	if request.method == 'POST' and 'loanappbtn' in request.POST:

		## If User is posting data using the button in our html named loanappbtn then we submit post to our form object

		businessform = BusinessApplication(request.POST)
		loanform = LoanApplication(request.POST)


		if businessform.is_valid() and loanform.is_valid():			# current_user = request.user
			
			# businessform.author = current_user.username
			businessform.save()
			# new_business.author = User.id
			loan_form = loanform.save(commit=False)
			# loan_form.business_id = request.new_business.id
			loanform.save()

			return redirect('home')
		else:
			messages.ERROR(request, f'Ensure loan is between 10000-100000 ')
			return redirect('loan_url')

## We are loading the forms for users that have not completed them 
	else:
		businessform = BusinessApplication()
		loanform = LoanApplication()
		template = 'accounts/businessregister.html'
		context = {'businessform': businessform, 'loanform':loanform}

	return render(request, template, context)
	


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
	return redirect('login')




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



# @login_required(login_url='login')
# def products(request):
# 	products = Product.objects.all()

# 	return render(request, 'accounts/products.html', {'products':products})

# @login_required(login_url='login')
# def customer(request, pk_test):
# 	customer = Customer.objects.get(id=pk_test)

# 	orders = customer.order_set.all()
# 	order_count = orders.count()

# 	myFilter = OrderFilter(request.GET, queryset=orders)
# 	orders = myFilter.qs 

# 	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
# 	'myFilter':myFilter}
# 	return render(request, 'accounts/customer.html',context)

# @login_required(login_url='login')
# def createOrder(request, pk):
# 	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
# 	customer = Customer.objects.get(id=pk)
# 	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
# 	#form = OrderForm(initial={'customer':customer})
# 	if request.method == 'POST':
# 		#print('Printing POST:', request.POST)
# 		form = OrderForm(request.POST)
# 		formset = OrderFormSet(request.POST, instance=customer)
# 		if formset.is_valid():
# 			formset.save()
# 			return redirect('/')

# 	context = {'form':formset}
# 	return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# def updateOrder(request, pk):

# 	order = Order.objects.get(id=pk)
# 	form = OrderForm(instance=order)

# 	if request.method == 'POST':
# 		form = OrderForm(request.POST, instance=order)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context = {'form':form}
# 	return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# def deleteOrder(request, pk):
# 	order = Order.objects.get(id=pk)
# 	if request.method == "POST":
# 		order.delete()
# 		return redirect('/')

# 	context = {'item':order}
# 	return render(request, 'accounts/delete.html', context)