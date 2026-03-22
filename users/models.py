import generate_code
from django.db import models
from django.contrib.auth.models import User

from datetime import timedelta
from uuid import uuid4
import random
from django.utils import timezone

class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name="uuid")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=255, null=True, blank=True)
    card_expiration_date = models.DateField(null=True, blank=True)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.card_number

    class Meta:
        db_table = "cards"


def generate_code():
    # 100000 dan 999999 gacha random son
    return random.randint(100000, 999999)


def exp_time_now():
    # Hozirdan 2 daqiqa keyin muddati tugaydi
    return timezone.now() + timedelta(minutes=2)

class VerificationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='verification_codes')
    code = models.PositiveIntegerField(default=generate_code)
    expired_date = models.DateTimeField(default=exp_time_now)

    def is_valid(self):
        """Kodning muddati o'tmagan bo'lsa True qaytaradi."""
        return timezone.now() <= self.expired_date

    def __str__(self):
        return f"{self.user.username} — Kod: {self.code}"

# Create your models here.
