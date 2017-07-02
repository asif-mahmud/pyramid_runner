import traceback
import logging

import pyramid.view as view

from . import base


class ErrorViews(base.BaseView):

    @view.forbidden_view_config()
    def not_allowed(self):
        return base.BaseJSONResponse(
            status="ERROR",
            code=403,
            msg='You are not permitted to access this URL.'
        )

    @view.notfound_view_config()
    def not_found(self):
        return base.BaseJSONResponse(
            status="ERROR",
            code=404,
            msg='Sorry, the requested service is not available.'
        )

    @view.exception_view_config()
    def server_error(self):
        logging.error(traceback.format_exc())
        return base.BaseJSONResponse(
            status="ERROR",
            code=500,
            msg='Sorry, something went wrong.'
                ' Please come back later.'
        )
