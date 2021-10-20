from django.urls import path
from .views import *

app_name = 'Usuario'

urlpatterns = [
    path('cadastro/', usuario_cadastro, name='cadastro'),
    path('login/', usuario_login, name='login'),
    path('logout/', usuario_logout, name='logout'),
]