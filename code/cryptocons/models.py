from django.db import models
from django.conf import settings


class Cards(models.Model):
    id = models.AutoField(primary_key=True)
    card_name = models.CharField(max_length=100)
    qr_code = models.CharField(max_length=100)
    image_location = models.ImageField(upload_to='cards/')
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
