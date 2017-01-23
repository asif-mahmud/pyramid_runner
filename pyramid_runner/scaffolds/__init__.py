from pyramid.scaffolds import PyramidTemplate
import sys


class PyramidRunnerProjectTemplate(PyramidTemplate):
    """
    Project template for sqlalchemy.
    """
    _template_dir = 'pyramid_runner'
    summary = 'Pyramid Runner Project Scaffold'

    def pre(self, command, output_dir, vars):
        vars['project_path'] = output_dir
        vars['project_venv'] = sys.prefix
        return PyramidTemplate.pre(self, command, output_dir, vars)
