from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from shows.models import Event
from shows.tests.utils import ObjectCreatorShows

class EventTest(APITestCase):

    def setUp(self):
        self.place = ObjectCreatorShows.create_place()
        self.event = ObjectCreatorShows.create_event(place=self.place)
        self.section = ObjectCreatorShows.create_section(place=self.place)
        self.chair = ObjectCreatorShows.create_chair(section=self.section)

    def test_get_event_ok(self):
        """
        Get all the Event objects
        """

        response = self.client.get(
            reverse('event'),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.json()[0].keys(),
        set(['pk', 'place', 'name', 'description', 'date',
            'start_time', 'end_time', 'status'])
        )

    def test_get_event_characteristic(self):
        """
        Get the characteristic from a event
        """
        data = {
            'pk': self.event.pk,
        }
        response = self.client.get(
            reverse('event-characteristic', kwargs=data),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(list(response.json()[0].keys()),
        ['event_name', 'event_description', 'date', 'start_time',
            'place_address', 'place_capacity'])