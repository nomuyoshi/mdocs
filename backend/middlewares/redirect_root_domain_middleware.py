from django.http import HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin


class RedirectRootDomainMiddleware(MiddlewareMixin):
    """
    This middleware removes "www.", and redirect to root domain urls.
    """
    def process_request(self, request):
        host = request.get_host()
        if host and host.startswith('www.'):
            redirect_url = '%s://mdoc.me%s' % (
                request.scheme, request.get_full_path()
            )
            return HttpResponsePermanentRedirect(redirect_url)
