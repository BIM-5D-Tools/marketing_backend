# backend/config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Nhóm toàn bộ endpoint vào /api/v1/
api_v1_patterns = [
    path("", include("apps.marketing.urls")),
    path("", include("apps.services.urls")),
    path("", include("apps.projects.urls")),
    path("", include("apps.news.urls")),
    path("", include("apps.contacts.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_v1_patterns)),
]

# Hỗ trợ xem ảnh / media file trực tiếp khi chạy Localhost
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
