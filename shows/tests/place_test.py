from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from shows.models import Place
from shows.tests.utils import ObjectCreatorShows

class PlaceTest(APITestCase):

    def setUp(self):
        self.place = ObjectCreatorShows.create_place()
        self.url =  reverse('place')

    def test_get_place_ok(self):
        """
        Get all the Place objects
        """
        response = self.client.get(
            self.url,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.json()[0].keys(),
        set(['pk', 'name', 'description', 
            'capacity', 'address'])
        )