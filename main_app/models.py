from django.db import models
from datetime import date

# Create your models here.

MATERIALS = (
    ('L', 'Leaf'),
    ('F', 'Flower'),
    ('R', 'Root'),
    ('B', 'Bark'),
    ('E', 'Berry'),
)

STATES = (
    ('F', 'Fresh'),
    ('D', 'Dried')
)

class Herb(models.Model):
    
    name = models.CharField(max_length=100)
    material = models.CharField(
        max_length=1,
        choices=MATERIALS,
        default=MATERIALS[0][0]
    )
    state = models.CharField(
        max_length=1,
        choices=STATES,
        default=STATES[0][0]
    )
    properties = models.TextField(max_length=500)
    image = models.CharField(max_length=100, default='https://i.postimg.cc/0NQ0ty2L/65411-E92-1783-46-D3-907-F-7-FA037834-E9-E.jpg')
        
    def __str__(self):
        return self.name

class Tincture(models.Model):
    name = models.CharField(max_length=100)
    solvent = models.CharField(max_length=100)
    herbs = models.ManyToManyField(Herb)
    image = models.CharField(max_length=100, default='https://i.postimg.cc/T3hVGrk7/Default.jpg')
        
    def __str__(self):
        return self.name
    
class Batch(models.Model):
    prep_date = models.DateField('prep date')
    ready_date = models.DateField('ready date')
    tincture = models.ForeignKey(Tincture, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"New Batch prepped on {self.prep_date}. To be strained and bottled on {self.ready_date}"
    
    class Meta:
        ordering = ['-prep_date']