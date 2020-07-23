# Modelo de la rama jess (comentarios).

from django.db import models
#importar de establecimientos
from establecimientos.models import Establishment

#Creacion de modelos iniciales para comentarios de producto.58
class Commentary(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre", null=True)
    content = models.TextField(verbose_name="Opinión")
    score = models.PositiveIntegerField(verbose_name="Estrellas")
    id_establecimiento = models.ForeignKey(Establishment, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural ="Comentarios"

#Configuracion de la funcion __str__ 62
    def __str__(self):
        return self.content

    