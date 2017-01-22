import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='pyramid_runner',
    version='0.0.1',
    author='Asif Mahmud Shimon',
    email='ams.eee09@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    requires=[
        'pyramid',
        'sqlalchemy',
    ],
    entry_points="""\
            [pyramid.scaffold]
            ring=pyramid_ring.scaffolds:PyramidRingProjectTemplate
            """,
)
