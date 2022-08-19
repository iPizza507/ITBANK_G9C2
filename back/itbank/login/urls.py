from django.urls import path
from . import views

urlpatterns = [
    # el home, antes del logueo
    path('', views.index, name='index'),
    # para loguearse
    path('login', views.login, name='login'),
    # Las vostas dentro del login
    path('homeIndex/', views.homeCuentas, name='homeCuentas'),
    path('homeIndex/homeTarjetas', views.homeTarjetas, name='homeTarjetas'),
]
