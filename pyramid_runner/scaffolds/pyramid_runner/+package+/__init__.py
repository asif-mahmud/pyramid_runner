from pyramid.config import Configurator
from pyramid.renderers import JSON


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_renderer(None, JSON())   # Add JSON as default renderer
    config.include('.models')
    config.include('.resources')
    config.scan()
    return config.make_wsgi_app()
