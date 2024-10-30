from rest_framework.routers import DefaultRouter

from appointments.apis.v1 import AppointmentViewSet

app_name = "appointments"
router = DefaultRouter()

router.register(r"", AppointmentViewSet, basename="appointment")
urlpatterns = router.urls
