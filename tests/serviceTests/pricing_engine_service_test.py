from unittest import TestCase
from _pytest import unittest

from src import application


class PricingEngineServiceTest(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.application = application.test_client()
        self.application.testing = True

    def tearDown(self):
        pass

    def test_root(self):
        result = self.application.get('/')
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
