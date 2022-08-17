from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


# donde el usuario se va a loguear
def login(request):
    return render(request, 'login/login.html')


# el inicio de todo
def index(request):
    return render(request, 'login/index.html')


# Todas las vistas de Home..

def homeCuentas(request):
    return render(request, 'login/Home/HomeCuentas.html')


def homeTarjetas(request):
    return render(request, 'login/Home/HomeTarjetas.html')
