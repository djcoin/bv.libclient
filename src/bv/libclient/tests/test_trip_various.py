"""Test scenario:

Testing various stuff here.

"""

import unittest
from unittest import TestCase

from bv.libclient.libtrips import LibTrips

class TestTripScenario1(TestCase):

    def setUp(self):
        # real test server url - no trailing slash ! -
        self.lt = LibTrips(server_url="http://127.0.0.1:8085")

    def tearDown(self):
        pass

    def XXXtest_counttrip(self):
        nb_trips = self.lt.count_trips()
        self.assertEquals(nb_trips, 0, "Still no trip provided")

    def test_listtrip(self):
        response = self.lt.list_trips()
        # fix me

    def test_getcities(self):
        prefix = "Pari"
        cities = self.lt.get_cities(prefix)
        l = [c for c in cities if prefix in c['name']]
        self.assertEquals(len(cities), len(l), "We retrieve all cities with the right prefix")

if __name__ == "__main__":
    unittest.main()
