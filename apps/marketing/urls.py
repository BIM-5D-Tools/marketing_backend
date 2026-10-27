# backend/apps/company/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeroBannerViewSet, CompanyMetricViewSet

router = DefaultRouter()
router.register(r"hero-banners", HeroBannerViewSet, basename="hero-banner")
router.register(r"company-metrics", CompanyMetricViewSet, basename="company-metric")

urlpatterns = [
    path("", include(router.urls)),
]
