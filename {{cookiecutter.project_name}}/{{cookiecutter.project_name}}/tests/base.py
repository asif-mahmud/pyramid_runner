import unittest
import transaction

from pyramid import testing
from webtest import TestApp


def dummy_request(dbsession):
    return testing.DummyRequest(dbsession=dbsession)


class BaseFunctionalTest(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'
        })
        from .. import main
        app = main({}, **self.config.get_settings())
        self.test_app = TestApp(app=app)


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'
        })
        self.config.include('.models')
        settings = self.config.get_settings()

        from ..models import (
            get_engine,
            get_session_factory,
            get_tm_session,
            )

        self.engine = get_engine(settings)
        session_factory = get_session_factory(self.engine)

        self.session = get_tm_session(session_factory, transaction.manager)

    def init_database(self):
        from ..models.meta import Base
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        from ..models.meta import Base

        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(self.engine)