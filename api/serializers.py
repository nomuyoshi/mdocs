from rest_framework import serializers
from .models import Document, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class DocumentSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Document
        fields = ('id', 'user', 'title', 'body', 'tags', 'created_at', 'updated_at')

