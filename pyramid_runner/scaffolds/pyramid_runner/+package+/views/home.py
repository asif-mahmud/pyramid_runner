from pyramid.view import (
    view_defaults,
    view_config
)
from ..resources import Root
from .base import BaseView


@view_defaults(context=Root)
class HomeView(BaseView):

    @view_config(name='')
    def hello_world(self):
        return dict(
            msg='Hello World!',
        )
