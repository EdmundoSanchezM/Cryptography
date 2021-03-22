"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from example.views import MainPage, VigenerePage, CifrarVigenere, DescifrarVigenere, AffinePage, CifrarAffine, DescifrarAffine
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', MainPage, name='index'),
    path('Vigenere/', VigenerePage, name='vigenere'),
    path('Affine/', AffinePage, name='affine'),
    path('CypherTxtVigenere/<filetxt>/<key>', CifrarVigenere),
    path('DecipherTxtVigenere/<filetxt>/<key>', DescifrarVigenere),
    path('CypherTxtAffine/<filetxt>/<a>/<b>/<alphabet>', CifrarAffine),
    path('DecipherTxtAffine/<filetxt>/<a>/<b>/<alphabet>', DescifrarAffine)

]

urlpatterns += staticfiles_urlpatterns()