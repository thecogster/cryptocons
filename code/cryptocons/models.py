from django.db import models
from django.conf import settings


class Cards(models.Model):
    id = models.AutoField(primary_key=True)
    leprechaun_number = models.CharField(max_length=100)
    tier = models.CharField(max_length=100, default=0)
    position = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True)
