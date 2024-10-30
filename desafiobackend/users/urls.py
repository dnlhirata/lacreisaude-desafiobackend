from rest_framework.routers import DefaultRouter

from users.apis.v1 import ProfessionalViewSet

app_name = "users"
router = DefaultRouter()

router.register(r"", ProfessionalViewSet, basename="professional")
urlpatterns = router.urls
