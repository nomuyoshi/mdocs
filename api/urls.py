from rest_framework import routers
from django.urls import path

from .views import DocumentViewSet, TagListView, UserDeleteView, ContactView

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'docs', DocumentViewSet, 'documents')

urlpatterns = [
    path('tags/', TagListView.as_view(), name="tag-list"),
    path('user/delete/', UserDeleteView.as_view(), name="user-delete"),
    path('contact/', ContactView.as_view(), name="contact"),
]

urlpatterns += router.urls
