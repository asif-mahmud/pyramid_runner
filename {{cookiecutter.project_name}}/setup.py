import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_tm',
    'SQLAlchemy',
    'psycopg2',
    'transaction',
    'zope.sqlalchemy',
    'gunicorn',
    'gevent',
    'bcrypt',
    'alembic',
    'pyramid_jwt',
    ]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    ]

setuptools.setup(
    name='{{cookiecutter.project_name}}',
    version='{{cookiecutter.project_version}}',
    description='{{cookiecutter.project_description}}',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP :: RESTful",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    url='{{cookiecutter.url}}',
    keywords='web wsgi bfg pylons pyramid sqlalchemy restful',
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points="""\
        [paste.app_factory]
        main = {{cookiecutter.project_name}}:main
        """,
)
