import {{cookiecutter.project_name}}.views.base as base


class AccessForbiddenError(base.BaseErrorReport):
    """Error message for access forbidden type error."""

    __code__ = 403
    __msg__ = 'You are not permitted to perform this action.'


class URLNotFoundError(base.BaseErrorReport):
    """Error message for resource not found type errors."""

    __code__ = 404
    __msg__ = 'The requested resource is not found.'


class ServerError(base.BaseErrorReport):
    """Error message for exceptions inside the server application."""

    __code__ = 500
    __msg__ = 'Sorry, something went wrong! Please come back later.'
