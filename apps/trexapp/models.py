from django.db import models

# Create your models here.

class Socio(models.Model):
    nome = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome