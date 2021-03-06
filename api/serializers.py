from rest_framework import serializers
from .models import Document, Tag

class TagSerializer(serializers.ModelSerializer):
    documents_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = ('id', 'name', 'documents_count')

class DocumentSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Document
        fields = ('id', 'user', 'title', 'body', 'tags', 'pin','created_at', 'updated_at')
        read_only_fields = ('id', 'user')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        doc = Document.objects.create(**validated_data)
        tags = self.__tag_list(tags_data, validated_data['user'])
        doc.tags.set(tags)
        return doc

    def update(self, instance, validated_data):
        if 'tags' in validated_data:
            tags_data = validated_data.pop('tags')
            tags = self.__tag_list(tags_data, validated_data['user'])
            instance.tags.set(tags)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def __tag_list(self, tags_data, user):
        tags = []
        for tag_data in tags_data:
            tag = Tag.objects.get_or_create(user=user, name=tag_data['name'])[0]
            tags.append(tag)
        return tags

