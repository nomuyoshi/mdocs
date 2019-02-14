import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET

from ..models import Document

@require_GET
def index(request):
    docs = Document.objects.order_by('-created_at').values()
    return JsonResponse({ 'docs': list(docs) })

@require_POST
def create(request, title, body):
    doc = Document(title = title, body = body)
    doc.save()
    return JsonResponse({ 'doc': doc })

