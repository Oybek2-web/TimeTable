from django.db import models
from django.contrib.auth.models import User


class Magazin(models.Model):
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='video/', blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=13, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='magazin_profil')

    profil_photo = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    about_you = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Category'

class Savol(models.Model):
    nom = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="savollar")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Tanlash(models.Model):
    savol = models.ForeignKey(Savol, on_delete=models.CASCADE, related_name="variantla")
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text