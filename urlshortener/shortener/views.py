from django.shortcuts import render, redirect, get_object_or_404
from .forms import URLForm
from .models import ShortURL
from django.utils import timezone


def home(request):
    form = URLForm()
    short_url = None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            short = form.save()
            short_url = request.build_absolute_uri('/') + short.short_code
    return render(request, 'shortener/home.html', {'form': form, 'short_url': short_url})


def redirect_to_original(request, code):
    url = get_object_or_404(ShortURL, short_code=code)
    if url.expires_at < timezone.now():
        return render(request, 'shortener/expired.html')
    url.clicks += 1
    url.save()
    return redirect(url.original_url)
