from django.db import models
#importar de productos
# Create your models here.58
#Creacion de modelos iniciales para comentarios de producto
class Commentary(models.Model):
    #
    #
    content = models.TextField(verbose_name="Opinión")
    score = models.PositiveIntegerField(verbose_name="Estrellas")
#Configuracion de la funcion __str__ 62
    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural ="Comentarios"
