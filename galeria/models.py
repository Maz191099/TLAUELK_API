from django.db import models

# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(upload_to='image', verbose_name="Imagen")

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural ="Galerias"