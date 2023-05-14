from cryptocons.models import Cards
from django.core.files import File
import os

# Create a new card object
new_card = Cards(card_name="My Card", qr_code="12345")

# Open the image file from the static folder
image_path = os.path.join("static", "images/logo.png")
with open(image_path, "rb") as f:
    # Save the image file to the database
    django_file = File(f)
    new_card.card_image.save("/images/logo.png", django_file, save=True)

# Save the new card object to the database
new_card.save()