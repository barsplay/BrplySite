from django.http import HttpResponse
from django.shortcuts import render
from .models import Advertisement

def index(request):
    advertisement = Advertisement.objects.all()
    context = {
        "advertisements": advertisement
    }
    return render(request, "index.html", context)

def top_sellers(request):
    return render(request, "top-sellers.html")

def advertisement_post(request):
    return render(request, "advertisement-post.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def profile(request):
    return render(request, "profile.html")