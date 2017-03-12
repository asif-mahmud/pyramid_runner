import os
import unittest

import transaction
import pyramid.testing as testing
import webtest


def dummy_request(dbsession):
    return testing.DummyRequest(dbsession=dbsession)


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:',
        })
        settings = self.config.get_settings()

        import {{cookiecutter.project_name}}.models as models

        self.engine = models.get_engine(settings)
        session_factory = models.get_session_factory(self.engine)

        self.session = models.get_tm_session(session_factory, transaction.manager)

    def init_database(self):
        from {{cookiecutter.project_name}}.models.meta import Base
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        # from ..models.meta import Base

        testing.tearDown()
        transaction.abort()
        # Base.metadata.drop_all(self.engine)


class BaseFunctionalTest(BaseTest):

    def setUp(self):
        super().setUp()
        # self.init_database()
        from {{cookiecutter.project_name}} import main
        app = main({}, **self.config.get_settings())
        self.test_app = webtest.TestApp(app=app)
