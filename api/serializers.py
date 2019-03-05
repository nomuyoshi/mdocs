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
        read_only_fields = ('id', 'user')

    # TODO: transaction
    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        doc = Document.objects.create(**validated_data)

        tags = []
        for tag_data in tags_data:
            tag = Tag.objects.get_or_create(user=validated_data['user'], name=tag_data['name'])[0]
            if tag: tags.append(tag)

        doc.tags.set(tags)
        return doc
