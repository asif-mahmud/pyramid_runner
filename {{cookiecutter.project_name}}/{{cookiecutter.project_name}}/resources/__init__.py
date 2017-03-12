from . import root


def includeme(config):
    config.set_root_factory(root.Root)
