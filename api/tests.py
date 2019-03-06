import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from api.models import Document
from api.factories import UserFactory, DocumentFactory, TagFactory

class DocumentsApiTest(APITestCase):
    def setUp(self):
        self.current_user = UserFactory.create(username='test-user1')
        self.tag = TagFactory.create(user=self.current_user, name="django")
        self.document = DocumentFactory.create(user=self.current_user)
        self.other_user_document = DocumentFactory.create(user=UserFactory.create())
        self.document.tags.add(self.tag)

    def test_documents_detail_response(self):
        """
          test document detail api response
        """
        client = APIClient()
        client.force_login(self.current_user, backend=None)
        url = reverse('documents-detail', kwargs={ 'pk': self.document.id })

        response = client.get(url, None, format='json')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], self.document.id)
        self.assertEqual(data['user'], self.current_user.id)
        self.assertEqual(data['title'], 'タイトル')
        self.assertEqual(data['body'], 'ドキュメントの内容')
        self.assertEqual(len(data['tags']), 1)
        self.assertEqual(data['tags'][0]['name'], 'django')

    def test_can_not_access_other_user_documents_detail(self):
        """
          test can not get other user's document
          return 404
        """
        client = APIClient()
        client.force_login(self.current_user, backend=None)
        url = reverse('documents-detail', kwargs={ 'pk': self.other_user_document.id })

        response = client.get(url, None, format='json')
        self.assertEqual(response.status_code, 404)
