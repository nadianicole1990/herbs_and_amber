from django.db import models

# Create your models here.
class Tincture(models.Model):
    name = models.CharField(max_length=100)
    herbs = models.CharField(max_length=100)
    solvent = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name