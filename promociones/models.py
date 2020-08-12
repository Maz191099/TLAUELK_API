from django.db import models
# Create your models here.

class Promotions(models.Model):
    image = models.ImageField(upload_to='image', verbose_name="Imagen")
    description = models.TextField(verbose_name="Descripción", null=True)

    class Meta:
        verbose_name = "Promocion"
        verbose_name_plural ="Promociones"

#Configuracion de la funcion __str__ 62
    def __str__(self):
        return self.description