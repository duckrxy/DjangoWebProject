"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Relevance(models.Model):
    item1 = models.TextField()
    item2 = models.TextField()

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    class Meta:
        ordering = ('item1', 'item2')
    
