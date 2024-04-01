from rest_framework import serializers

from shows.models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'pk', 'place', 'name', 'description', 'date',
            'start_time', 'end_time', 'status',
            )