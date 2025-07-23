from django.db import models
import string, random
from django.utils import timezone
from datetime import timedelta

def default_expiry():
    return timezone.now() + timedelta(days=7)

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    expires_at = models.DateTimeField(default=default_expiry)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
