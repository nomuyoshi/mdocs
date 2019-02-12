import json
from django.http import HttpResponse

def index(request):
    docs = [
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

    data = { 'data': docs }
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=None)
    return response

