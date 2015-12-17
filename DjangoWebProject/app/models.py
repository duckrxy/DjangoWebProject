"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Relevance(models.Model):
    item1 = models.CharField(max_length=20, blank=True, default='')
    item2 = models.CharField(max_length=20, blank=True, default='')

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    class Meta:
        ordering = ('item1',)
    
