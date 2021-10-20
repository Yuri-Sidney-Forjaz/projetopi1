from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
     path('entidades_parceiras', views.entidades, name='entidades'),
     path("home", views.home, name='home'),
     path("sobre", views.sobre, name='sobre'),
     path("voluntario", views.voluntario, name='voluntario')
]

