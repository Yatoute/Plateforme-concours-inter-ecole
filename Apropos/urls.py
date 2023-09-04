from django.contrib import admin 
from django.urls import path 
from . import views # Du dossier local, importe views
urlpatterns = [
    path('', views.Apropos_view, name='Apropos'),
   
    
]