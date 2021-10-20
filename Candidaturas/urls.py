from django.urls import path

from .views import *

app_name = 'candidatura'

urlpatterns = [
    path('nova_candidatura/Apae/', candidatura_criarApae, name='apae'),
    path('nova_candidatura/Abbc/', candidatura_criarAbbc, name='abbc'),
    path('<id>/detalhe/', candidatura_detalhe, name='detalhe'),
    path('todas/', candidatura_todas, name='todas'),
]