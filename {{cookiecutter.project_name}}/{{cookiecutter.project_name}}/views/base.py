from pyramid.request import Request


class BaseView(object):
    """Base helper class for view classes.

    Provides a default `__init__` method.

    Attributes:
        request(pyramid.request.Request): Current `Request` instance
    """

    def __init__(self, request):
        if isinstance(request, Request):
            self.request = request
