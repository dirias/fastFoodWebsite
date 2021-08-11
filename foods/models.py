from typing_extensions import Required
from django.db import models

# Create your models here.

class Foods(models):
    
    name = models.CharField(max_length=100, Require=True)
    description = models.CharField(max_length=300, Required=True)
    type_food = models.CharField(max_length=100, Required=True)
    price = models.IntegerField(Required=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)