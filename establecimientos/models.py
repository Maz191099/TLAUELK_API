from django.db import models
from django.contrib.auth.models import User
# Modelo de la rama larios (establecimientos).

class Establishment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    image = models.ImageField(upload_to='image', verbose_name="Imagen")
    direction = models.TextField(verbose_name="Dirección")
    description = models.TextField(verbose_name="Descripción", null=True)
    schedule = models.CharField(max_length=255, verbose_name="Horario")
    id_user = models.ForeignKey(User, verbose_name="Usuario" , on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Establecimiento"
        verbose_name_plural ="Establecimientos"

    def __str__(self):
        return self.name