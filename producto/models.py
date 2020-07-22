from django.db import models

#Modelo creado en la rama sandy referente a producto.

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    image =models.ImageField(upload_to='imageprod', verbose_name="Imagen")
    description = models.TextField()
