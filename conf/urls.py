from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('', include('gestao_notas.urls', namespace='gestao_notas')),
    path('ceo-controler/', admin.site.urls),
]
