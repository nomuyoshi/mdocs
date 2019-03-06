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
        tags = self.__tag_list(tags_data)
        doc.tags.set(tags)
        return doc

    # TODO: transaction
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        tags = self.__tag_list(tags_data)
        instance.tags.set(tags)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

    def __tag_list(tags_data):
        tags = []
        for tag_data in tags_data:
            tag = Tag.objects.get_or_create(user=validated_data['user'], name=tag_data['name'])[0]
            tags.append(tag)
        return tags

