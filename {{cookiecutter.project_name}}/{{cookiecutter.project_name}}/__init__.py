import pyramid.config
import pyramid.renderers as renderers


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = pyramid.config.Configurator(settings=settings)
    # Add JSON as default renderer
    config.add_renderer(None, renderers.JSON())
    config.include('pyramid_jwt')
    config.include('.security')
    config.include('.models')
    config.include('.resources')
    config.scan()
    return config.make_wsgi_app()
