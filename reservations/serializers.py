from datetime import date

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Property, Booking


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        validators = (
            UniqueTogetherValidator(
                queryset=Booking.objects.all(),
                fields=('property', 'start_date', 'end_date'),
                message="This booking overlaps with an existing booking."
            ),
        )
    
    def validate_start_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Start date must be in the future.")
        return value

    def validate(self, data):
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data