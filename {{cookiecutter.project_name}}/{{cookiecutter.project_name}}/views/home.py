import pyramid.view as view

from . import base
import {{cookiecutter.project_name}}.resources.root as root


@view.view_defaults(context=root.Root)
class HomeView(base.BaseView):

    @view.view_config(name='', request_method='GET')
    def hello_world(self):
        return base.BaseJSONResponse(
            msg='Welcome to {{cookiecutter.project}}!',
        )
