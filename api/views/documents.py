import json
from django.http import JsonResponse
from ..models import Document

def index(request):
    docs = Document.objects.order_by('-created_at').values()
    return JsonResponse({ 'docs': list(docs) })

