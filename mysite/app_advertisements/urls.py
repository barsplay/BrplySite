from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="index"),
    path('top-sellers/', top_sellers, name="sellers"),
    path('advertisement-post/', advertisement_post, name="advertisement-post"),
]
