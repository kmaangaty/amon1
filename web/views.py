from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home_view(*args, **kwargs):
    return HttpResponse('<h1>This is home_view page<h1>')


def login_view(*args, **kwargs):
    return HttpResponse('<h1>This is login_view page<h1>')


def register_view(*args, **kwargs):
    return HttpResponse('<h1>This is register_view page<h1>')
