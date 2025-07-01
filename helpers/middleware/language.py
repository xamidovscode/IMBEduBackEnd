from django.utils import translation


class LanguageMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.GET.get('lang') or request.headers.get("Accept-Language", "en")
        translation.activate(lang)
        response = self.get_response(request)
        translation.deactivate()
        return response
