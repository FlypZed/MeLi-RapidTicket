from django.db import models

from shows.models import Place

class Section(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
        )
    place = models.ForeignKey(
        Place, 
        on_delete=models.CASCADE, 
        null=models.CASCADE,
        )