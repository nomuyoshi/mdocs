from django.db import transaction
from django.db.models import Count
from django.contrib.auth import logout

from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .slack_client import SlackClient
from .models import Document, Tag
from .serializers import DocumentSerializer, TagSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        current_user = self.request.user
        params = self.request.query_params
        query_set = current_user.document_set

        if params.get('tag', None):
            try:
                tag = current_user.tag_set.get(name=params.get('tag'))
            except Tag.DoesNotExist:
                return Document.objects.none()
            query_set = tag.document_set

        if params.get('title', None):
            query_set = query_set.filter(title__icontains=params.get('title'))

        return query_set.prefetch_related('tags').order_by('-created_at')

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

class UserDeleteView(generics.DestroyAPIView):

    def get_object(self):
        return self.request.user

    def peform_destroy(self, instance):
        logout(self.request)
        instance.delete()

class ContactView(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data['text']
        user = self.request.user
        message =  user.username + '(' + user.email + ')' + 'より問い合わせ\n\n' + text
        if SlackClient().post(message):
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
