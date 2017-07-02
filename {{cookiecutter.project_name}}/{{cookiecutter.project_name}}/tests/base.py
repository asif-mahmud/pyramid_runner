"""Helper classes for tests.

Provides -
    1. dummy_request(dbsession): A `DummyRequest` instance.
    2. BaseTest: Base test class that includes a database
        session.
    3. BaseFunctionalTest: Base test class that includes
        a `test_app` for cheking out the routes.
"""
import os
import unittest

import transaction
import pyramid.paster as paster
import pyramid.testing as testing
import webtest

import {{cookiecutter.project_name}} as services
import {{cookiecutter.project_name}}.models as models
import {{cookiecutter.project_name}}.models.meta as meta


def dummy_request(dbsession):
    """Returns instance of `pyramid.testing.DummyRequest`."""
    return testing.DummyRequest(dbsession=dbsession)


class BaseTest(unittest.TestCase):
    """Base test class.

    Attributes:
        config: Application configuration
        engine: DB Engine
        session: DB Session instance
    """

    maxDiff = None

    def get_settings(self):
        """Publice method to expose the application settings `dict`."""
        settings = paster.get_appsettings(
            os.path.join(
                os.path.abspath(
                    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
                ),
                'development.ini'
            )
        )
        return settings

    def setUp(self):
        """Defines useful variables and initializes database.

        After this, following variables will be available-
            1. config: Application configuration
            2. engine: DB engine
            3. session: DB session instance
        """
        settings = self.get_settings()

        self.config = testing.setUp(settings=settings)

        self.engine = models.get_engine(settings)
        session_factory = models.get_session_factory(self.engine)

        self.session = models.get_tm_session(
            session_factory,
            transaction.manager
        )

        self.__init_database()

    def __init_database(self):
        """Initialize the database models.

        Define a method called `init_db` to initialize
        any database instance. This method will automatically
        be called at `setUp`.

        Caution: If `init_db` is defined, a `clean_db` method
        should also be defined which will be called at
        `tearDown`.
        """
        meta.Base.metadata.create_all(self.engine)

        try:
            __init_db = self.__getattribute__('init_db')
            if callable(__init_db):
                with transaction.manager:
                    __init_db()
        except AttributeError:
            pass

    def tearDown(self):
        """Calls `pyramid.testing.tearDown` and `transaction.abort`.

        Prior to calling these methods if any `clean_db` method is
        defined, it will be called. Do database clean ups there.
        """
        try:
            __clean_db = self.__getattribute__('clean_db')
            if callable(__clean_db):
                with transaction.manager:
                    __clean_db()
        except AttributeError:
            pass

        testing.tearDown()
        transaction.abort()


class BaseFunctionalTest(BaseTest):
    """Base test class for functional tests.

    Attributes:
        test_app(webtest.TestApp): A test wsgi app instance.
    """

    def setUp(self):
        app = services.main({}, **self.get_settings())
        self.test_app = webtest.TestApp(app=app)
        super().setUp()

    def tearDown(self):
        super().tearDown()
