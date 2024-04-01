from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from shows.serializers import EventSerializer, EventCharacteristicSerializer
from shows.models import Event


class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [
        DjangoFilterBackend, 
        filters.OrderingFilter,
        filters.SearchFilter
        ]

class EventCharacteristicAPIView(generics.ListAPIView):
    serializer_class = EventCharacteristicSerializer
    def get(self, request, pk):
        queryset = Event.objects.filter(pk=pk)

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)