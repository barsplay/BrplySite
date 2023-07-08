from django.http import HttpResponse
from django.shortcuts import render

def output(request):
    return HttpResponse('Домашка по 4 занятию')
