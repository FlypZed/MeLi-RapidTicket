from rest_framework import serializers

from shows.models import Chair, Section

class ChairSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chair
        fields = (
            'pk', 'name', 'section', 'aviable',
             'buyer_name', 'buyer_dni',
            )

class SectionChairSerializer(serializers.ModelSerializer):
    chair_id = serializers.IntegerField()
    chair_name = serializers.CharField()
    aviable_id = serializers.BooleanField()
    section_name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def to_representation(self, instance):
        section = instance.section
        return {
            'chair_id': instance.pk,
            'chair_name': instance.name,
            'aviable': instance.aviable,
            'section_name': section.name,
            'price': section.price,
        }