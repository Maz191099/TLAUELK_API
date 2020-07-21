from django.db import models

# Create your models here.58
#Creacion de modelos iniciales para comentarios de producto
class Commentary(models.Model):
    
    content = models.TextField()
    score = models.PositiveIntegerField()
