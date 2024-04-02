# Instructivo de Pruebas para Meli - Rapid Ticket en Django y Django RestFramework

## Objetivo

Este instructivo tiene como objetivo guiar al equipo de desarrollo en la realización de pruebas unitarias y de integración para el proyecto RapidTicket en Django utilizando Django Rest Framework (DRF).

### Definición de modelos

Para el ejercicio en cuestion se crearon cuatro modelos (tablas) para la base de datos:

- Event: Represente un evento artisitico individual, como un concierto o una obra de teatro
- Place: Lugar fisico donde se presentara el evento
- Section: Subdivision de la sala con diferentes precios y ubicaciones
- Chair: Representacion de la silla o espacio disponible individual

### Definicion de API's

Con el fin de hacer uso de las funcionalidades propuestas (Poder listar los shows y funciones disponibles con todas sus características,  Para una función de un show deberá ser posible listar las butacas disponibles con su respectivo precio y por último deberá poderse realizar una reserva de la función, indicando DNI, nombre del espectador y los lugares con el precio registrando todo a modo de ticket de reserva.) se generaron tres API's estas son:

- EventCharacteristicAPIView (./chair-event/<int:pk>)
- ChairListEventAPIView (./event-characteristic/<int:pk>)
- PurchaseChairAPIView (./purchase-chair/<int:pk>')

## Requisitos previos

- Instalación de Python 3.12.2 o superior, Django y Django Rest Framework.
- Configuración de un entorno virtual para el proyecto.

## Pasos a seguir

### Preparación del entorno de pruebas

Asegúrese de haber activado el entorno virtual del proyecto.

- Para activar el entorno virtual del proyecto:
   1. Abra una terminal desde la rama del proyecto
   2. en la terminal puede ejecutar el comando: ' .\venv\scripts\activate '
- Posiblemente tambien sera necesario hacer las migraciones para el correcto funcionamiento de la base de datos, para esto:
   1. Con el enotorno virtual ya activo ejecute las siguientes instrucciones:
      ' python manage.py makemigrations '
      ' python manage.py migrate '

### Ejecucion de pruebas unitarias

Para la ejecucion de pruebas unitarias se creo un archivo independiente para cada modelo, las pruebas de funcionalidad fueron escritas en sus correspondientes archivos dependiendo del objeto principal que se busca de la base de datos. Para ver la ejecucion de cada una de estas, puede ejecutar los siguientes comandos dentro del entorno virtual.

   1. ' python manage.py test shows.tests.chair_test '
   2. ' python manage.py test shows.tests.event_test '
   3. ' python manage.py test shows.tests.place_test '
   4. ' python manage.py test shows.tests.section_test '

### Mantenimiento de pruebas

1. Actualice y mantenga las pruebas a medida que se realizan cambios en el código base.
2. Asegúrese de que las pruebas continúen siendo relevantes y proporcionen una cobertura adecuada para todas las funcionalidades importantes de la aplicación.

### Aclaracion acerca de pruebas en rapid-ticket-ml.azurewebsites.net

Al desplegar una aplicación en un entorno de producción, puede resultar desafiante ejecutar pruebas de forma efectiva debido a limitaciones en el acceso a la base de datos y el riesgo de afectar el funcionamiento en vivo de la aplicación. Para abordar esto, se opto por recurrir a técnicas que utilizan datos estáticos para simular el comportamiento de la base de datos durante las pruebas.

En este enfoque común se utilizo un archivo JSON para almacenar datos de prueba que pueden ser cargados en la aplicación durante la ejecución de las pruebas.

Sin embargo, es importante tener en cuenta algunas limitaciones:

- **Limitación de datos**: Los datos en el archivo JSON son estáticos y limitados en comparación con una base de datos completa, lo que puede limitar la exhaustividad de las pruebas.

## Recursos adicionales

- [Documentación oficial de Django](https://docs.djangoproject.com/)
- [Documentación oficial de Django Rest Framework](https://www.django-rest-framework.org/)
- [Documentación de pruebas en Django](https://docs.djangoproject.com/en/stable/topics/testing/)
- [Tutorial de pruebas en Django Rest Framework](https://www.django-rest-framework.org/api-guide/testing/)