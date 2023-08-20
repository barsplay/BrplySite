from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementForm

from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse

def index(request):
    advertisement = Advertisement.objects.all()
    context = {
        "advertisements": advertisement
    }
    return render(request, "app_advertisements/index.html", context)

def top_sellers(request):
    return render(request, "app_advertisements/top-sellers.html")


def advertisement_post(request:WSGIRequest):
    
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()

            return redirect(
                reverse("index")
            )
    else:
        form = AdvertisementForm()
    context = {
        'form':form
    }
    return render(request, "app_advertisements/advertisement-post.html", context)