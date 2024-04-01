from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from shows.views import (
    SectionListCreateAPIView, EventListCreateAPIView,
    PlaceListCreateAPIView, ChairListCreateAPIView,
    ChairListEventAPIView, EventCharacteristicAPIView
)

urlpatterns = format_suffix_patterns([
    path(
        'section/',
        SectionListCreateAPIView.as_view(),
        name='section'
    ),
    path(
        'event/',
        EventListCreateAPIView.as_view(),
        name='event'
    ),
    path(
        'place/',
        PlaceListCreateAPIView.as_view(),
        name='place'
    ),
    path(
        'chair/',
        ChairListCreateAPIView.as_view(),
        name='chair'
    ),
    path(
        'chair-event/<int:pk>',
        ChairListEventAPIView.as_view(),
        name='chair-event'
    ),
    path(
        'event-characteristic/<int:pk>',
        EventCharacteristicAPIView.as_view(),
        name='event-characteristic'
    ),
])
