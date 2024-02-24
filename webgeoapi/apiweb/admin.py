from django.contrib import admin

# Register your models here.
from .models import Sitio,OrdenServicio 

admin.site.register(Sitio)
#admin.site.register(OrdenServicio)

#@admin.register(Sitio)
#class SitioAdmin(admin.ModelAdmin):
    #list_display = ('nombre','latitud','longitud','direccion','imagen', 'fecha_registro')