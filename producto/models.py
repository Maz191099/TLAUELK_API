from django.db import models
from establecimientos.models import Establishment

#Modelo creado en la rama sandy referente a producto.

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    image =models.ImageField(upload_to='image', verbose_name="Imagen")
    description = models.TextField(verbose_name="Descripción")
    precio = models.CharField(max_length=255, verbose_name="Precio $")
    id_establishment = models.ForeignKey(Establishment, verbose_name="Establecimiento", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        
    def __str__(self):
        return self.name
    