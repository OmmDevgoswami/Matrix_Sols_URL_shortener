from django.contrib import admin
from .models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'created_at', 'clicks', 'expires_at')
