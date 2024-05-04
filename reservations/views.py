from rest_framework import viewsets

from .models import Property, Booking
from .serializers import PropertySerializer, BookingSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'tenant':
            return Booking.objects.filter(tenant=user)
        elif user.user_type == 'owner':
            return Booking.objects.filter(property__owner=user)
        return super().get_queryset()
