from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('Usuario.urls')),
    path('', include('blog.urls')),
    path('formularios/', include('formularios.urls')),
    path('candidatura/', include('Candidaturas.urls')),
]
