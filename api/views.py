from rest_framework import viewsets, filters
from .models import Document
from .serializers import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.order_by('-created_at').all()
    serializer_class = DocumentSerializer
