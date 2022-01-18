from rest_framework.routers import DefaultRouter

from locations.views import GeolocationViewSet

router = DefaultRouter()
router.register(r'geolocations', GeolocationViewSet, basename='geolocations')

urlpatterns = router.urls
