from . import base


class TestCORSHeaders(base.BaseFunctionalTest):

    def test_origin_access(self):
        res = self.test_app.get('/')
        self.assertEqual(res.headers.get('Access-Control-Allow-Origin'), '*')

    def test_method_access(self):
        expected_methods = (
            'POST',
            'GET',
            'PUT',
            'DELETE',
            'OPTIONS',
        )
        res = self.test_app.get('/')
        res_methods = res.headers.get('Access-Control-Allow-Methods').split(',')
        found_methods = list()
        for method in res_methods:
            found_methods.append(method.strip())
        for method in expected_methods:
            self.assertIn(method, found_methods)
