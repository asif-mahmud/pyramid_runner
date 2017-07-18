import traceback
import logging

import pyramid.view as view

from . import base
import {{cookiecutter.project_name}}.views.errors as errors


class ErrorViews(base.BaseView):

    @view.forbidden_view_config()
    def not_allowed(self):
        return errors.AccessForbiddenError()

    @view.notfound_view_config()
    def not_found(self):
        return errors.URLNotFoundError()

    @view.exception_view_config()
    def server_error(self):
        self.log_error(
            self.server_error,
            str(self.request.exception)
        )
        return errors.ServerError()
