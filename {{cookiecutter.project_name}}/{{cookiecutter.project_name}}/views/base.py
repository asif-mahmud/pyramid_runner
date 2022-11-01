import logging
import datetime

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

    def log_error(self, method, error):
        """Log error messages from the views."""
        logging.error(
            '[{}] From {}.{}: {}'.format(
                datetime.datetime.now().isoformat(),
                self.__class__.__name__,
                method.__name__,
                error
            )
        )


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


class BaseStatusReport(BaseJSONResponse):
    """Base class to represent a status report.

    This class basically sets the foure attributes -
    `code`, `status`, `msg`, `error` from class level
    attributes `__code__`, `__status__`, `__msg__` and
    `__error__` respectively. It may be useful to define
    some status report standards for the API.

    Aside from that, this can be used just like the
    `BaseJSONResponse`.

    Usage:
    ```
    class LoginSuccessReport(BaseStatusReport):
        __code__ = 100
        __status__ = 'OK'
        __msg__ = 'You are logged in'
        __error__ = ''
    ```
    """

    def __init__(self, *args, code=200, status="OK",
                 msg="", error="", **kwargs):
        super().__init__(
            *args, code=code, status=status, msg=msg,
            error=error, **kwargs
        )
        for attr in (
            '__code__',
            '__status__',
            '__msg__',
            '__error__',
        ):
            if hasattr(self, attr):
                setattr(
                    self,
                    attr.replace('_', ''),
                    getattr(self, attr)
                )


class BaseErrorReport(BaseStatusReport):
    """Helper base class to build error reports.

    Attributes:
        __status__(str): Defaults to **ERROR**.
    """

    __status__ = 'ERROR'


class BaseSuccessReport(BaseStatusReport):
    """Helper base class to build success reports.

    Attributes:
        __status__(str): Defaults to **OK**.
    """

    __status__ = 'OK'
