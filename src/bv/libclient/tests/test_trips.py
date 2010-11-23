"""Test scenario:

Testing various stuff here.

"""

import unittest
from unittest import TestCase

from bv.libclient.libtrips import LibTrips


from bv.libclient.baselib import BaseLib, BvResource
from bv.libclient.tests.helpers import get_authent_lib

class TestTripScenario1(TestCase):

    def setUp(self):
        BaseLib._resource_class = get_authent_lib('toto', 'tototo')
        # real test server url - no trailing slash ! -
        self.lt = LibTrips(server_url="http://127.0.0.1:8085")

    def tearDown(self):
        BaseLib._resource_class = BvResource

    # def test_create_trip(self):
    #     nb_trips = self.lt.count_trips()
    #     self.assertEquals(nb_trips, 0, "Still no trip provided")

    def FAILXXXtest_test(self):
        self.lt.list_user_trips()

    def test_test(self):
        import pdb; pdb.set_trace()
        self.lt.add_trip(*{})


if __name__ == "__main__":
    unittest.main()
