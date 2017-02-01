from .base import BaseFunctionalTest


class TestHomeView(BaseFunctionalTest):

    def test_home_msg(self):
        res = self.test_app.get('/')
        self.assertEqual(res.json["msg"], "Hello World!")
