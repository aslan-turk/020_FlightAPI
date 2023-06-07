from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Passenger,PassengerSerializer,
    Flight,FlightSerializer,
    Reservation,ReservationSerializer
)

#!------------------------- Fix View ------------------------------

class FixView(ModelViewSet):
    pass

#!------------------------- Passenger View ------------------------------

class PassengerView(FixView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

#!------------------------- Flight View ------------------------------
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class FlightView(FixView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
#!------------------------- Reservation View ------------------------------

class ReservationView(FixView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer