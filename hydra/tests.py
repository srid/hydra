import unittest
from pyramid import testing

class ViewTests(unittest.TestCase):

    def setUp(self):
        testing.setUp()
        
    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from hydra.views import my_view
        context = testing.DummyModel()
        request = testing.DummyRequest()
        response = my_view(context, request)
        self.assertEqual(response['project'], 'hydra')

