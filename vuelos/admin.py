from django.contrib import admin
from .models import Aeropuerto,Vuelo

admin.site.register(Vuelo)
# Register your models here.
admin.site.register(Aeropuerto)