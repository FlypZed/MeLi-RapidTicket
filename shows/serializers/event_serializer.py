from rest_framework import serializers

from shows.models import Event, Place

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'pk', 'place', 'name', 'description', 'date',
            'start_time', 'end_time', 'status',
            )
    
class EventCharacteristicSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField()
    event_description = serializers.CharField()
    date = serializers.DateField()
    start_time = serializers.DateTimeField()
    place_address = serializers.CharField()
    place_capacity = serializers.IntegerField()

    def to_representation(self, instance):
        place = instance.place
        return {
            'event_name': instance.name,
            'event_description': instance.description,
            'date': instance.date,
            'start_time': instance.start_time,
            'place_address': place.address,
            'place_capacity': place.capacity,
        }