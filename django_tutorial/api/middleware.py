from django.utils.deprecation import MiddlewareMixin


class TestMiddleWare(MiddlewareMixin):

    def process_requests(self, request):
        consumer_key = request.META.get("HTTP_X_CONSUMER_KEY", None)