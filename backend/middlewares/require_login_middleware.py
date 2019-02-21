from django.http import HttpResponse
import re
import pdb

class RequoreLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.url_pattern = r'^/api/*'

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            return None

        if re.match(self.url_pattern, request.path):
            return HttpResponse('Unauthorized', status=401)

        return None

