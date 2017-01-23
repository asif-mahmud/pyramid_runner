from pyramid.config import Configurator
from .root import Root


def includeme(config):
    if isinstance(config, Configurator):
        config.set_root_factory(Root)
