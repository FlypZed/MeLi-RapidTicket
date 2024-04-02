from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
import json

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
        # Intenta obtener los datos de la base de datos
        queryset = Event.objects.filter(pk=pk)
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
                for item in data:
                    if item["model"] == "shows.event" and item["pk"] == self.kwargs['pk']:
                      event_name = item["fields"]["name"]
                      event_description = item["fields"]["description"]
                      event_date = item["fields"]["date"]
                      event_start_time = item["fields"]["start_time"]

                      place_pk = item["fields"]["place"]
                      for place_item in data:
                        if place_item["model"] == "shows.place" and place_item["pk"] == place_pk:
                          place_address = place_item["fields"]["address"]
                          place_capacity = place_item["fields"]["capacity"]
                          break

                      return {
                          "event_name": event_name,
                          "event_description": event_description,
                          "event_date": event_date,
                          "event_start_time": event_start_time,
                          "place_address": place_address,
                          "place_capacity": place_capacity,
                      }
                # Devolver un mensaje de error si no se encuentra el registro
                return {"error": "No se encontraron datos para la pk especificada en el archivo JSON"}
        except Exception as e:
            return {"error": str(e)}