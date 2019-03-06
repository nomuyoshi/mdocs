from django.db import transaction
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer, TagSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        current_user = self.request.user
        return current_user.document_set.order_by('-created_at').all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer

    def get_queryset(self):
        current_user = self.request.user
        return current_user.tag_set.all()
