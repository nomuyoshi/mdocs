import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.forms.models import model_to_dict
from ..models import Document

@require_GET
def index(request):
    docs = Document.objects.order_by('-created_at').values()
    return JsonResponse({ 'docs': list(docs) })

@require_POST
def create(request):
    params = json.loads(request.body)
    doc = Document(title = params['title'], body = params['body'])
    doc.save()
    data = model_to_dict(doc)
    return JsonResponse({ 'doc': data })

