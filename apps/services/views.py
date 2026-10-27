from rest_framework import viewsets
from .models import BimServiceCategory
from .serializers import BimServiceCategorySerializer


class BimServiceCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BimServiceCategory.objects.filter(is_active=True)
    serializer_class = BimServiceCategorySerializer
    lookup_field = "slug"
