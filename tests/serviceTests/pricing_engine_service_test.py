from unittest import TestCase
from _pytest import unittest
import json

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

    def test_calculate_price_with_all_data(self):
        d = dict(host_split=50.0,
                 guest_price=4500.0,
                 channel_fees=10.5,
                 vat_percentage=20.0,
                 floor_price=1500)

        result = self.application.post('/host-pricing-engine/compute-price', data=d)
        json_data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertIsNotNone(result.data)
        self.assertIsNotNone(json_data['host_share'])
        self.assertIsNotNone(json_data['vat'])
        self.assertIsNotNone(json_data['ofs_share'])

    def test_not_calculate_price_without_all_data(self):
        d = dict()

        result = self.application.post('/host-pricing-engine/compute-price', data=d)

        self.assertEqual(result.status_code, 400)

    def test_not_calculate_price_with_partial_data(self):
        d = dict(host_split=50.0,
                 guest_price=4500.0,
                 channel_fees=10.5)

        result = self.application.post('/host-pricing-engine/compute-price', data=d)

        self.assertEqual(result.status_code, 400)

if __name__ == '__main__':
    unittest.main()
