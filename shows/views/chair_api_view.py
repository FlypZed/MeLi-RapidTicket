from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json

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
        if queryset.exists():  # Si hay datos en la base de datos
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:  # Si no hay datos en la base de datos, carga desde el archivo JSON
            data_from_json = self.load_data_from_json()
            return Response(data_from_json)

    def load_data_from_json(self):
        try:
            # Abre y carga el archivo JSON
            with open('shows.json', 'r',  encoding='utf-16') as json_file:
                data = json.load(json_file)
                available_seats = []
                for item in data:
                    if item["model"] == "shows.event" and item["pk"] == self.kwargs['pk']:
                        event_place_pk = item["fields"]["place"]
                        break
                
                for item in data:
                    if item["model"] == "shows.section" and item["fields"]["place"] == event_place_pk:
                        section_pk = item["pk"]
                
                for item in data:
                    if item["model"] == "shows.chair" and item["fields"]["aviable"] == True and item["fields"]["section"] == section_pk:
                        available_seats.append(item["fields"]["name"])

                return available_seats
                # Devolver un mensaje de error si no se encuentra el registro
                return {"error": "No se encontraron datos para la pk especificada en el archivo JSON"}
        except Exception as e:
            return {"error": str(e)}

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
