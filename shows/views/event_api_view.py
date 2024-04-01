from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from shows.serializers import EventSerializer
from shows.models import Event


class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [
        DjangoFilterBackend, 
        filters.OrderingFilter,
        filters.SearchFilter
        ]