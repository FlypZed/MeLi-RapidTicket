from rest_framework import serializers

from shows.models import Section

class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = (
            'pk', 'name', 'price', 'place',
            )