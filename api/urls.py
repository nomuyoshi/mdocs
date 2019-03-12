from rest_framework import routers
from django.urls import path

from .views import DocumentViewSet, TagListView

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'docs', DocumentViewSet, 'documents')

urlpatterns = [
    path('tags/', TagListView.as_view(), name="tag-list"),
]

urlpatterns += router.urls
