from django.db import transaction
from django.db.models import Count
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework import generics

from .models import Document
from .serializers import DocumentSerializer, TagSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        current_user = self.request.user
        query_set = current_user.document_set.prefetch_related('tags').order_by('-created_at').all()
        title = self.request.query_params.get('title', None)
        if title:
            query_set = query_set.filter(title__icontains=title)
        return query_set

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

class TagListView(generics.ListAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        current_user = self.request.user
        query_set = current_user.tag_set.annotate(documents_count=Count('document')).order_by('id').all()

        return query_set
