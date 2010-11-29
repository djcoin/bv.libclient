"""Test scenario:

Testing matching trips.

Test trips:
"""

import unittest
from bv.libclient.tests.helpers import TestMother
import bv.libclient.tests.helper_trip as helper_trip
from bv.libclient.tests.helper_trip import ServerCmd, get_valid_trip_full_data_v1

from bv.libclient.libtrips import LibTrips
from bv.libclient.exceptions import EditTripFormError

from restkit.errors import RequestFailed



# TODO
class TestTripMatching(TestMother):

    def setUp(self):
        super(TestTripMatching, self).setUp()
        self.lt = LibTrips(self.server_url)

        # api1
        # offer_trip = helper_trip.create_offer_trip(params)
        # demand_trip = helper_trip.create_matching_demand(offer_trip, params)

        # api2
        # otrip, dtrip = create_matching_couple(params)

        # self.srvcmd = ServerCmd(self.lt)
        # self.id_trip, _ = self.srvcmd.create_trip()
        # self._register_teardown(lambda: self.srvcmd.delete_trip(self.id_trip))

        pass
