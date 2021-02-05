try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

from .settings import *


class ClickCounterMiddleware(MiddlewareMixin):
    """
    This middleware will check if countclick in request.GET params,
    if provided then will add this value to records.
    """

    def process_request(self, request):
        if request.method == 'GET':
            if COUNTCLICK_GET_KEY in request.GET.keys():
                # It means should count clicks on this page. so store info
                print(request.GET[COUNTCLICK_GET_KEY])
        return request

