from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PropertyViewSet, BookingViewSet

router_v1 = DefaultRouter()
router_v1.register('properties', PropertyViewSet)
router_v1.register('bookings', BookingViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
