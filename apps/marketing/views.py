from rest_framework import viewsets
from .models import HeroBanner, CompanyMetric, PmisIntro
from .serializers import (
    HeroBannerSerializer,
    CompanyMetricSerializer,
    PmisIntroSerializer,
)


class HeroBannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HeroBanner.objects.filter(is_active=True)
    serializer_class = HeroBannerSerializer


class CompanyMetricViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CompanyMetric.objects.all()
    serializer_class = CompanyMetricSerializer


class PmisIntroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PmisIntro.objects.all()
    serializer_class = PmisIntroSerializer
