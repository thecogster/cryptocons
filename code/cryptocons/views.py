from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, CardsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import qrcode
import os
import mimetypes
import shutil
from .models import Cards
import datetime
from cryptocons.models import Cards

def home(request):

    template = 'cryptocons/homepage.html'
    return render(request, template)

@login_required(login_url='login_url')
def craicLounge(request):

	return render(request, 'cryptocons/craic_lounge.html')

@login_required(login_url='login_url')
def collectables(request):

	return render(request, 'cryptocons/collectables.html')


def register(request):

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

@login_required(login_url='login_url')
def qr_scan(request, api_package):

	user_id = request.user.id
    
	qr_package = api_packageparts = api_package.split('_')
	
	Cards.objects.filter(id=qr_package[3]).update(owner_id=user_id)

	os.mkdir(f"cryptocons/{qr_package[3]}")

	return render(request, 'cryptocons/qr_scan.html')

@login_required(login_url='login_url')
def qr_generator(request):
    template = 'cryptocons/qr_generator.html'

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        for i in range(1, int(quantity)):
            form = CardsForm(request.POST)
            form.save()

        # Get the form inputs from the POST request
        leprechaun_number = request.POST.get('leprechaun_number')
        tier_id = request.POST.get('tier')
        position = request.POST.get('position')
        quantity = request.POST.get('quantity')

        save_path = "cryptocons/static/images/qr/" + datetime.datetime.now().strftime("%Y:%M:%d")

        if not os.path.exists(save_path):
            os.makedirs(save_path)
            print(f"Directory '{save_path}' created successfully.")
        else:
            print(f"Directory '{save_path}' already exists.")
        
        num_of_cards = Cards.objects.all().count()

        for i in range(num_of_cards+1, num_of_cards+int(quantity)):
            url = "http://127.0.0.1:8000/qr_scan/" 

            # Combine the URL and unique ID
            data = url + str(leprechaun_number) + "_" + str(tier_id) + "_" + str(position) + "_" + str(i)

            # Generate the QR code
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(data)
            qr.make(fit=True)

            # Create an image from the QR code
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Save the QR code image with the unique ID as the filename
            qr_image.save(f"{save_path}/L{leprechaun_number}_T{tier_id}_P{position}_{i}.png")

        shutil.make_archive(f'{save_path}' + '/output', 'zip', save_path)
        zip_file = open(f'{save_path}' + '/output.zip', 'rb')
        return FileResponse(zip_file)

    return render(request, template)

# @login_required(login_url='login_url')
def leaderboard(request):
    # Retrieve all users and sort by date joined
    all_users = User.objects.order_by('date_joined')

	## Its a dictionary passed as users to html 
    return render(request, 'cryptocons/leaderboard.html', {'users': all_users})


@login_required(login_url='login_url')
def profile(request):

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
