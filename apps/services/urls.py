# backend/apps/services/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BimServiceCategoryViewSet

router = DefaultRouter()
router.register(r"bim-services", BimServiceCategoryViewSet, basename="bim-service")

urlpatterns = [
    path("", include(router.urls)),
]
