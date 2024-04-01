from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=100, null=False)
    capacity = models.IntegerField()
    description = models.TextField(blank=True)