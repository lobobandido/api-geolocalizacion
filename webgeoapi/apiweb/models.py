from django.db import models

# Create your models here.
class Sitio(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    direccion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='sitio', blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    #fecha_creacion = models.DateTimeField(default=timezone.now)
    
    

    def __str__(self):
        return self.nombre

class OrdenServicio(models.Model):
    numero = models.CharField(max_length=20)
    sitio = models.ForeignKey(Sitio, on_delete=models.RESTRICT)
    ingeniero_asig= models.TextField(null=True) 
    #fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    # Otros campos relevantes para la orden de servicio conforme avance definire q campos agregar 

    def __str__(self):
        return f'Orden de Servicio #{self.numero}'
