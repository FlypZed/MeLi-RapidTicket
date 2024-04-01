from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from shows.views import (
    SectionListAPIView, EventListAPIView,
    PlaceListAPIView, ChairListAPIView,
    ChairListEventAPIView, EventCharacteristicAPIView
)

urlpatterns = format_suffix_patterns([
    path(
        'section/',
        SectionListAPIView.as_view(),
        name='section'
    ),
    path(
        'event/',
        EventListAPIView.as_view(),
        name='event'
    ),
    path(
        'place/',
        PlaceListAPIView.as_view(),
        name='place'
    ),
    path(
        'chair/',
        ChairListAPIView.as_view(),
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
