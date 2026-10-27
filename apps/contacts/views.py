# apps/contacts/views.py
from rest_framework import viewsets, mixins
from .models import ContactRequest
from .serializers import ContactRequestSerializer


class ContactRequestViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer
