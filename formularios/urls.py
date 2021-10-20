from django.urls import path
from . import views

urlpatterns = [
    path('apae', views.apae, name='apae'),
    path('abbc', views.abbc, name='abbc'),
]
