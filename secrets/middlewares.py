from tokenapi.http import JsonError
from django.conf import settings
from django.http import HttpResponseRedirect

class ExceptionMiddleware(object):
    def process_exception(self, request, exception):
        return JsonError({'error': str(exception)})

class SSLMiddleware(object):
    def process_request(self, request):
        if not any([settings.DEBUG, request.is_secure(), request.META.get("HTTP_X_FORWARDED_PROTO", "") == 'https']):
            url = request.build_absolute_uri(request.get_full_path())
            secure_url = url.replace("http://", "https://")
            return HttpResponseRedirect(secure_url)