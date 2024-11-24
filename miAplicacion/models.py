from django.db import models

# Create your models here.

class productos(models.Model):
    codigoProducto = models.CharField(max_length=20)
    descripcionProducto = models.CharField(max_length=255)
    estatus = models.BooleanField()
    


