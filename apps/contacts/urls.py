# backend/apps/contacts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactRequestViewSet

router = DefaultRouter()
router.register(r'contact-submit', ContactRequestViewSet, basename='contact-submit')

urlpatterns = [
    path('', include(router.urls)),
]