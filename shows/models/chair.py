from django.db import models

from shows.models import Section, Event

class Chair(models.Model):

    name = models.CharField(max_length=50, null=False)
    aviable = models.BooleanField(null=False, default=True)
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        null=False,
        )