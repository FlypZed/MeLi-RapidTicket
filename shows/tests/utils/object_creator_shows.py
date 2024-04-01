from datetime import datetime
from shows.models import (
    Chair, Event, Place, Section
    )

class ObjectCreatorShows:

    @staticmethod
    def create_event(
        place=None,
        status=Event.ACTIVE,
        name="Test Event Name",
        description="Test Event Description",
        date=datetime.now(),
        start_time=datetime.now(),
        end_time=datetime.now(),
    ) -> Event:
        return Event.objects.create(
            place=place or ObjectCreatorShows.create_place(), 
            status=status,
            name=name,
            description=description,
            date=date,
            start_time=start_time,
            end_time=end_time,
        )

    @staticmethod
    def create_place(
        name="Test Place Name",
        description="Test Place Description",
        capacity=100,
        address="Test Place Address",
    ) -> Place:
        return(
            Place.objects.create(
                name=name,
                description=description,
                capacity=capacity,
                address=address,
            )
        )

    @staticmethod
    def create_section(
        place=None,
        name="Test Section Name",
        price=100,
    ) -> Section:
        return Section.objects.create(
            place=place or ObjectCreatorShows.create_place(),
            name=name,
            price=price,
        )

    def create_chair(
        name="Chair Name",
        aviable=True,
        section=None,
    ) -> Chair: 
        return Chair.objects.create(
            name=name,
            aviable=aviable,
            section=section or ObjectCreatorShows.create_section(),
        )