import json
from django.http import HttpResponse
import pdb;

def index(request):
    data = [
        {
            'id': 1,
            'title': 'djangoについて',
        },
        {
            'id': 2,
            'title': 'vueについて',
        },
        {
            'id': 3,
            'title': 'reactについて',
        }
    ]

    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=None)
    return response
