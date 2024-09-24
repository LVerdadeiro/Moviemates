"""
URL configuration for MovieMates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Movieapp import views

urlpatterns = [
    path('', views.lista_filmes, name='lista_filmes'),  # Página inicial
    path('sessao/<int:sessao_id>/', views.detalhe_sessao, name='detalhe_sessao'),  # Detalhes da sessão
    path('reservar/<int:assento_id>/', views.reservar_assento, name='reservar_assento'),  # Reservar assento
]
