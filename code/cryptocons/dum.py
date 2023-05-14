from django.contrib.auth.models import User
from cryptocons.models import Cards
from django.http import request# Get the current user
current_user = User.objects.get(username=request.user.username)

# Create a new Card object and save it to the database
new_card = Cards(card_name="Card 1", qr_code="1234", card_image="images/logo.png", owner=current_user)
new_card.save()