from django.db import models

from shows.models import Place

class Event(models.Model):

    ACTIVE = "ACTIVE"
    POSTPONED = "POSTPONED"
    CANCELLED = "CANCELLED"

    STATUS_CHOICES = (
        (ACTIVE, ACTIVE),
        (POSTPONED, POSTPONED),
        (CANCELLED, CANCELLED),
    )

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        null=False,
        )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True)
    date = models.DateField(null=False)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
