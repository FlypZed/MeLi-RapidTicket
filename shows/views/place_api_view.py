from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from shows.serializers import PlaceSerializer
from shows.models import Place


class PlaceListAPIView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [
        DjangoFilterBackend, 
        filters.OrderingFilter,
        filters.SearchFilter
        ]