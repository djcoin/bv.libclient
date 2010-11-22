"""Test scenarii"""

import unittest
from unittest import TestCase

from bv.libclient import LibTrips

class TestTripScenario1(TestCase):

    def setUp(self):
        # real test server url - no trailing slash ! -
        self.lt = LibTrips(server_url="http://127.0.0.1:8085")

    def tearDown(self):
        pass

    def test_counttrip(self):
        self.assertEquals(self.lt.count_trips(), 0, "Still no trip provided")

    def test_listtrip(self):
        response = self.lt.list_trips()

    def test_getcities(self):
        cities = self.lt.get_cities("Pari")
        # city.name, city.zipcode
        self.assertTrue(cities == [])

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestTripScenario1)
