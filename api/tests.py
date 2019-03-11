import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from api.models import Document
from api.factories import UserFactory, DocumentFactory, TagFactory

def api_client(user):
    client = APIClient()
    client.force_login(user, backend=None)
    return client

class DocumentsApiTest(APITestCase):
    def setUp(self):
        self.current_user = UserFactory.create(username='test-user1')
        self.tag = TagFactory.create(user=self.current_user, name="django")
        self.document = DocumentFactory.create(user=self.current_user)
        self.other_user_document = DocumentFactory.create(user=UserFactory.create())
        self.document.tags.add(self.tag)

    def test_documents_list_unauthorized_user_response(self):
        """
          when an unauthorized user requests api, return 401
        """
        url = reverse('documents-list')
        response = APIClient().get(url, None, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_documents_list_response(self):
        """
          test document list api response
          return 200
        """
        url = reverse('documents-list')
        response = api_client(self.current_user).get(url, None, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.current_user.id)

    def test_documents_detail_unauthorized_user_response(self):
        """
          when an unauthorized user requests api, return 401
        """
        url = reverse('documents-detail', kwargs={ 'pk': self.document.id })
        response = APIClient().get(url, None, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_documents_detail_response(self):
        """
          test document detail api response
          return 200
        """
        url = reverse('documents-detail', kwargs={ 'pk': self.document.id })
        response = api_client(self.current_user).get(url, None, format='json')
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
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
        url = reverse('documents-detail', kwargs={ 'pk': self.other_user_document.id })

        response = api_client(self.current_user).get(url, None, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_documents_create_response(self):
        """
          test document create api response
          return 201
        """
        url = reverse('documents-list')
        params = { 'title': 'title-test', 'body': 'body-test', 'tags': [] }
        response = api_client(self.current_user).post(url, params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], self.current_user.id)

    def test_documents_update_response(self):
        """
          test document update api response
          return 201
        """
        url = reverse('documents-detail', kwargs={ 'pk': self.document.id })
        params = {
            'title': 'title(updated)',
            'body': 'body(updated)',
            'tags': [
                {
                    'id': None,
                    'name': 'python3',
                }
            ],
        }
        response = api_client(self.current_user).put(url, params, format='json')
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['title'], 'title(updated)')
        self.assertEqual(data['body'], 'body(updated)')
        self.assertEqual(len(data['tags']), 1)
        self.assertEqual(data['tags'][0]['name'], 'python3')

    def test_documents_delete_unauthorized_user_response(self):
        """
          when an unauthorized user requests api, return 401
        """
        url = reverse('documents-detail', kwargs={ 'pk': self.document.id })
        response = APIClient().delete(url, None, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_documents_delete_response(self):
        """
          test document delete api response
          return 204
        """
        url = reverse('documents-detail', kwargs={ 'pk': self.document.id })

        response = api_client(self.current_user).delete(url, None, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
