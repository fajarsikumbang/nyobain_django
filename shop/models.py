# shop/models.py
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.URLField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
