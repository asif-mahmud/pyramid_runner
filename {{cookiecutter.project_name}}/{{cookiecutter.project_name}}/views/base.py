import pyramid.request as request
import pyramid.view as view


class BaseView(object):
    """Base helper class for view classes.

    Provides a default `__init__` method.

    Attributes:
        request(pyramid.request.Request): Current `Request` instance
    """

    def __init__(self, req):
        if isinstance(req, request.Request):
            self.request = req

    @view.view_config(name='', request_method='OPTIONS')
    def browser_friendly(self):
        """This method makes the view browser friendly."""
        return BaseJSONResponse()


class BaseJSONResponse(dict):
    """A Base response tupe to provide a consistent response for all views.

    It includes the following keys by default-
        1. code(int): HTTP response code or some meaningful code. Defaults 200.

        2. status(str): Some status string saying the success status of the
            request. Defaults "OK".

        3. msg(str): Some elaborating or human readable message about the
            operation result. Defaults "".

        4. error(str): If any error happens during the operation, corresponding
            error message. Defaults "".
    """

    def __init__(self, *args, code=200, status="OK",
                 msg="", error="", **kwargs):
        super().__init__(*args, **kwargs)
        self.__setitem__("code", code)
        self.__setitem__("status", status)
        self.__setitem__("msg", msg)
        self.__setitem__("error", error)

    @property
    def code(self):
        return self.__getitem__('code')

    @code.setter
    def code(self, code):
        self.__setitem__('code', code)

    @property
    def status(self):
        return self.__getitem__('status')

    @status.setter
    def status(self, status):
        self.__setitem__('status', status)

    @property
    def msg(self):
        return self.__getitem__('msg')

    @msg.setter
    def msg(self, msg):
        self.__setitem__('msg', msg)

    @property
    def error(self):
        return self.__getitem__('error')

    @error.setter
    def error(self, error):
        self.__setitem__('error', error)
