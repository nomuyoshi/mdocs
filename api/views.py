from rest_framework import viewsets, filters
from .models import Document
from .serializers import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        current_user = self.request.user
        return current_user.document_set.order_by('-created_at').all()
