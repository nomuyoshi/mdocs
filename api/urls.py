from rest_framework import routers
from .views import DocumentViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'docs', DocumentViewSet, 'documents')
router.register(r'tags', TagViewSet, 'tags')
