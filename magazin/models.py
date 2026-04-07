from django.db import models
from django.contrib.auth.models import User

class TimeTable(models.Model):
    kurs_nomi = models.CharField(max_length=50)
    auditoriya = models.CharField(max_length=255)
    start = models.TimeField()
    finish = models.TimeField()
    guruh = models.CharField(max_length=200)
    sana = models.DateTimeField()

    def __str__(self):
        return self.kurs_nomi

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='magazin_profil')
    profil_photo = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    about_you = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return self.name


# class Category(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         db_table = 'Category'
#
# class Savol(models.Model):
#     nom = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="savollar")
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.nom
#
#
# class Tanlash(models.Model):
#     savol = models.ForeignKey(Savol, on_delete=models.CASCADE, related_name="variantla")
#     text = models.CharField(max_length=200)
#     is_correct = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.text