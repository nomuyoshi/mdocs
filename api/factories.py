import factory
from . import models
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Sequence(lambda n: 'first_name%d' % n)
    last_name = factory.Sequence(lambda n: 'last_name%d' % n)
    username = factory.Sequence(lambda n: 'username%d' % n)
    password = 'password'
    email = factory.Sequence(lambda n: 'user%d@example.com' % n)

class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Document

    title = 'タイトル'
    body = 'ドキュメントの内容'

class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tag

    name = factory.Sequence(lambda n: 'tag%d' % n)

