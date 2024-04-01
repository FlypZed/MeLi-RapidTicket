from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.response import Response

from shows.serializers import ChairSerializer, SectionChairSerializer
from shows.models import Chair


class ChairListCreateAPIView(generics.ListCreateAPIView):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializer
    filter_backends = [
        DjangoFilterBackend, 
        filters.OrderingFilter,
        filters.SearchFilter
        ]

class ChairListEventAPIView(generics.ListAPIView):
    serializer_class = SectionChairSerializer

    def get(self, request, pk):
        queryset = Chair.objects.filter(
            Q(section__place__event__pk=pk) &
            Q(aviable=True)
            )

        serializer = self.serializer_class(queryset, many=True)
        
        return Response(serializer.data)