from . import base


class TestHomeView(base.BaseFunctionalTest):

    def test_home_get(self):
        res = self.test_app.get('/')
        self.assertEqual(res.json['status'], 'OK')
        self.assertEqual(res.json['code'], 200)
        self.assertEqual(res.json["msg"], "Hello World!")

    def test_home_options(self):
        res = self.test_app.options('/')
        self.assertEqual(res.json['status'], 'OK')
        self.assertEqual(res.json['code'], 200)
        self.assertEqual(res.json["msg"], "")
