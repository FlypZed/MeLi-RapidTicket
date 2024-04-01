from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from shows.models import Chair, Section
from shows.tests.utils import ObjectCreatorShows

class ChairTest(APITestCase):

    def setUp(self):
        self.place = ObjectCreatorShows.create_place()
        self.event = ObjectCreatorShows.create_event(place=self.place)
        self.section = ObjectCreatorShows.create_section(place=self.place)
        self.chair = ObjectCreatorShows.create_chair(section=self.section)

    def test_get_chair_ok(self):
        """
        Get all the Chair objects
        """
        response = self.client.get(
            reverse('chair'),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(list(response.json()[0].keys()),
        ["pk", "name", "section", "aviable", 'buyer_name', 'buyer_dni']
        )

    def test_get_chair_event_ok(self):
        """
        Get all the Chair objects by the Event element
        """
        chair01 = ObjectCreatorShows.create_chair(section=self.section)
        chair02 = ObjectCreatorShows.create_chair(section=self.section)
        chair03 = ObjectCreatorShows.create_chair(section=self.section)
        chair04 = ObjectCreatorShows.create_chair(section=self.section)

        data={
            'pk': self.event.pk,
        }
        response = self.client.get(
            reverse('chair-event', kwargs=data),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(list(response.json()[0].keys()),
        ['chair_id', 'chair_name', 'aviable',
         'section_name', 'price']
        )

    def test_get_only_chair_aviable(self):
        """
        Get all the Chair objects by the Event element
        """
        chair01 = ObjectCreatorShows.create_chair(section=self.section)
        chair02 = ObjectCreatorShows.create_chair(section=self.section)
        chair03 = ObjectCreatorShows.create_chair(section=self.section, aviable=False)
        chair04 = ObjectCreatorShows.create_chair(section=self.section, aviable=False)
        
        data={
            'pk': self.event.pk,
        }
        response = self.client.get(
            reverse('chair-event', kwargs=data),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(list(response.json()[0].keys()),
        ['chair_id', 'chair_name', 'aviable',
         'section_name', 'price']
        )
    
    def test_buy_chair(self):
        """
        Buy a chair
        """
        data = {
            'pk': self.chair.pk,
            'chair_name': self.chair.name,
            'buyer_name': 'John Smith',
            'buyer_dni': '161803390'
        }
        response = self.client.post(
            reverse('purchase-chair', args=(self.chair.pk,)),
            data=data,
            format='json'
        )
        buyed_chair = Chair.objects.get(pk=self.chair.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(buyed_chair.buyer_dni, '161803390')
        self.assertEqual(buyed_chair.aviable, False)