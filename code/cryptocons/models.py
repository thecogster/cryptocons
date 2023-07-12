from django.db import models
from django.conf import settings
from django.core.files import File
import random
import os
from django.contrib.auth.models import AbstractUser

def generate_random_number():
    return random.randint(1000000, 9999999)

class CardsModel(models.Model):
    id = models.AutoField(primary_key=True)
    leprechaun_number = models.CharField(max_length=10)
    tier = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    validation_code = models.IntegerField(default=generate_random_number)
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def save(self, *args, **kwargs):
        if not self.pk or self._state.adding or 'image' in self.get_dirty_fields():
            image_path = f"cryptocons/static/images/character_images/P{self.position}/L{self.leprechaun_number} T{self.tier} P{self.position}.png"
            image_file = open(image_path, 'rb')
            self.image.save(
                f"P{self.position}/L{self.leprechaun_number} T{self.tier} P{self.position}.png",
                File(image_file),
                save=False
            )
            image_file.close()
        return super().save(*args, **kwargs)

    def get_dirty_fields(self):
        dirty_fields = []
        for field in self._meta.fields:
            if field.attname not in ["id", "created_date"] and getattr(self, field.attname) != getattr(self._original, field.attname):
                dirty_fields.append(field.attname)
        return dirty_fields
      
class Announcement(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title