from django.urls import path
from . import views

urlpatterns = [
    path('', views.jogo, name='jogo'),
    path('reiniciar/', views.reiniciar, name='reiniciar'),
]