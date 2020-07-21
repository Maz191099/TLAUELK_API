from django.db import models

# Create your models here.58
#Creacion de modelos iniciales para comentarios de producto
class Commentary(models.Model):
    
    content = models.TextField()
    score = models.PositiveIntegerField()
#Configuracion de la funcion __str__ 62
    def __str__(self):
        return self.content
