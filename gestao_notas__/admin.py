from django.contrib import admin
from .models import Person

# Aqui você pode registrar seu modelo Person para aparecer no admin do Django
admin.site.register(Person)
