from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        current_user = self.request.user
        return current_user.document_set.order_by('-created_at').all()

    def create(self, request, *args, **kwargs):
        # current_userをセットするためにオーバーライド
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
