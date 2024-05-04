from django.core.validators import MinValueValidator
from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Property(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='properties')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class Booking(models.Model):
    tenant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        unique_together = ('property', 'start_date', 'end_date')

    def __str__(self):
        return f"{self.tenant.username} - {self.property.name} from {self.start_date} to {self.end_date}"
