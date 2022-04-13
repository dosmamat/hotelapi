from rest_framework import viewsets

from .serializers import HotelSerializer, RoomSerializer
from .models import Hotel, Room


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer