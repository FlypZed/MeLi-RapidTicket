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
    buyer_dni = models.CharField(max_length=50, null=True, blank=True)
    buyer_name = models.CharField(max_length=100, null=True, blank=True)

    def clean(self):
        if not self.aviable and not self.buyer_id and not self.buyer_name:
            raise ValidationError("Si la silla no está disponible, debe especificarse quién la compró.")