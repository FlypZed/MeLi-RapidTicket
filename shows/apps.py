from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils import timezone
from datetime import timedelta

class ShowsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shows'

    def ready(self):
        from .models import Place, Section, Event, Chair

        def load_data(sender, **kwargs):
            print("Cargando datos iniciales...")

            # Crear lugares famosos
            theater1 = Place.objects.create(
                name="Teatro Colón", 
                address="Calle 10 #5-32, Bogotá", 
                capacity=5000, 
                description="Uno de los teatros más importantes de América Latina"
                )
            theater2 = Place.objects.create(
                name="Teatro Nacional de Costa Rica", 
                address="Calle 3, Avenida 2, San José", 
                capacity=1200, 
                description="El principal teatro de Costa Rica"
                )

            # Crear secciones para los lugares
            section1_theater1 = Section.objects.create(
                name="Platea", 
                price=100.00, 
                place=theater1
                )
            section2_theater1 = Section.objects.create(
                name="Balcón", 
                price=50.00, 
                place=theater1
                )

            section1_theater2 = Section.objects.create(
                name="General", 
                price=20.00, 
                place=theater2
                )

            # Crear eventos
            event1 = Event.objects.create(
                place=theater1, 
                status=Event.ACTIVE, 
                name="Concierto de Orquesta", 
                description="Una noche de música clásica con la Orquesta Sinfónica Nacional", 
                date=timezone.now().date() + timedelta(days=30), 
                start_time="19:00", 
                end_time="21:00"
                )
            event2 = Event.objects.create(
                place=theater2, 
                status=Event.ACTIVE, 
                name="Obra de Teatro",
                description="Una comedia teatral imperdible", 
                date=timezone.now().date() + timedelta(days=45), 
                start_time="20:00", 
                end_time="22:00"
                )

            # Crear sillas para cada evento
            for event in [event1, event2]:
                for section in event.place.section_set.all():
                    for i in range(10):  # Máximo 10 sillas por sección
                        Chair.objects.create(name=f"Silla {i+1}", aviable=True, section=section)

        post_migrate.connect(load_data, sender=self)
