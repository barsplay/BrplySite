from django.urls import path
from .views import output

urlpatterns = [
    path('lesson_4/', output)
]
