from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users_profil')
    profil_photo = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    about_you = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return self.name