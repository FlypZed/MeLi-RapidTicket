from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from shows.serializers import SectionSerializer
from shows.models import Section


class SectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filter_backends = [
        DjangoFilterBackend, 
        filters.OrderingFilter,
        filters.SearchFilter,
        ]