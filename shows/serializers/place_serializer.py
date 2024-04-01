from rest_framework import serializers

from shows.models import Place

class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = (
            'pk', 'name', 'description', 
            'capacity', 'address',
            )