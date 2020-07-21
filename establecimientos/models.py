from django.db import models

# Modelo de la rama larios (establecimientos).

class Establishment(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image')
    direction = models.TextField()
    schedule = models.CharField(max_length=255)

