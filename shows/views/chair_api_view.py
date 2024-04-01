from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

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

class PurchaseChairAPIView(APIView):
    def post(self, request, *args, **kwargs):
        pk = request.data.get('pk')
        chair_name = request.data.get('name')
        buyer_dni = request.data.get('buyer_dni')
        buyer_name = request.data.get('buyer_name')

        try:
            chair = Chair.objects.get(pk=pk, aviable=True)
        except Chair.DoesNotExist:
            return Response({"error": "La silla no está disponible o no existe."}, status=status.HTTP_400_BAD_REQUEST)

        section_price = chair.section.price
        chair.aviable = False
        chair.buyer_dni = buyer_dni
        chair.buyer_name = buyer_name
        chair.save()

        serializer = ChairSerializer(chair)

        return Response(serializer.data, status=status.HTTP_200_OK)
