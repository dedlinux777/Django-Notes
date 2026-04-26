from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Station
from .serializers import StationSerializer

class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    # A. Overriding Default Methods: perform_create
    # Useful for logging or adding data the user didn't provide
    def perform_create(self, serializer):
        print(f"Adding new station data for: {self.request.data.get('name')}")
        serializer.save()

    # B. Using the @action Decorator: Custom endpoint
    # Access this at: /api/stations/all_names/
    @action(detail=False, methods=['get'])
    def all_names(self, request):
        names = Station.objects.values_list('name', flat=True)
        return Response(names)

    # Access this at: /api/stations/1/ping/
    @action(detail=True, methods=['get'])
    def ping(self, request, pk=None):
        station = self.get_object()
        return Response({'status': f'Station {station.name} is active and reporting.'})


    # how does django know that the ping method is for /api/stations/1/ping/ this api only?
    # Because of the @action decorator with detail=True,
    # Django REST Framework automatically generates a URL pattern for this method that includes the primary key (pk) of the station instance.
    # So when you access /api/stations/1/ping/, it will call the ping method for the station with pk=1.
    # then lets say if I access /api/stations/1/ponng what will happen?
    # If you access /api/stations/1/ponng, you will get a 404 Not Found error because there is no URL pattern defined for "ponng".
    # The @action decorator only creates a URL pattern for the "ping" method, so any other URL that does not match the defined patterns will result in a 404 error.
    # what if I access /api/stations/1/pingg?
    # If you access /api/stations/1/pingg, you will also get a 404 Not Found error for the same reason as above.
    # The URL pattern for the "ping" method is specifically defined as /api/stations/<pk>/ping/,
    # so the url pattern is created based on method name, like the ping method will create a url pattern with ping in it,
    # so if you change the method name to pingg then the url pattern will also change to /api/stations/<pk>/pingg/ and
    # if you try to access /api/stations/1/pingg/ then it will work
    # but if you try to access /api/stations/1/ping/ then it will give you a 404 error because there is no url pattern for ping anymore.