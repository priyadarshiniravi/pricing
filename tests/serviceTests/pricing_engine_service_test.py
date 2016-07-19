from unittest import TestCase

import pytest
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
        with application.test_client() as client:
            response = client.post('/host-pricing-engine/compute-price', data=json.dumps(d),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)

    def test_not_calculate_price_without_all_data(self):
        d = dict()

        response = self.application.post('/host-pricing-engine/compute-price', data=json.dumps(d),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_not_calculate_price_with_partial_data(self):
        d = dict(host_split=50.0,
                 guest_price=4500.0,
                 channel_fees=10.5)

        response = self.application.post('/host-pricing-engine/compute-price', data=json.dumps(d),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
