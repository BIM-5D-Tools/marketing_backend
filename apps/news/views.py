# apps/news/views.py
from rest_framework import viewsets
from .models import NewsArticle
from .serializers import NewsArticleSerializer


class NewsArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsArticle.objects.all().order_by("-published_at")
    serializer_class = NewsArticleSerializer
    lookup_field = "slug"
