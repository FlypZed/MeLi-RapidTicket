from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from shows.models import Section
from shows.tests.utils import ObjectCreatorShows

class SectionTest(APITestCase):

    def setUp(self):
        self.section = ObjectCreatorShows.create_section()
        self.url =  reverse('section')

    def test_get_section_ok(self):
        """
        Get all the Place objects
        """
        response = self.client.get(
            self.url,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.json()[0].keys(),
        set(['pk', 'name', 'price', 'place',])
        )