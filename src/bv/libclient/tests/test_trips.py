"""Test scenario:

Testing trips stuff

"""

import unittest
from bv.libclient.tests.helpers import TestMother
import bv.libclient.tests.helper_trip as helper_trip
from bv.libclient.tests.helper_trip import ServerCmd

from bv.libclient.libtrips import LibTrips

from restkit.errors import RequestFailed

###
### FIXME: for update/delete tests, trip should already be in the database
###        and those trips should be automatically created/destroyed 
###        (at creation time to)

class TestTripAdd(TestMother):
# class TestTripAdd(object):

    def setUp(self):
        super(TestTripAdd, self).setUp()
        self.lt = LibTrips(self.server_url)
        self.srvcmd = ServerCmd(self.lt)

    def test_add_trip_fail_missing_args(self):
        try:
            self.lt.add_trip(**{})
        except Exception, e:
            return
        self.fail("Trips arguments missing: should throw exception")

    def test_add_trip_fail_wrong_args(self):
        dct = {'dummyvalue1': 0,
               'dummyvalue2': 1,}
        try:
            wtf = self.lt.add_trip(**dct)
        except RequestFailed, e:
            return
        self.fail("Trips arguments erroneous: should throw exception")

    def test_add_trip_with_erroneous_arg_should_success(self):
        dct = helper_trip.get_valid_trip_full_data()
        dct['erroneous key'] = "erroneous value"

        trip = self.lt.add_trip(**dct)
        self.assertTrue(trip.id, "The trip has been created with a valid id!")

        self.srvcmd.delete_trip(trip.id)

    def test_add_trip_success(self):
        dct = helper_trip.get_valid_trip_full_data()

        trip = self.lt.add_trip(**dct)
        self.assertTrue(trip.id, "The trip has been created with a valid id!")

        self.srvcmd.delete_trip(trip.id)



class TestTripDelete(TestMother):
# class TestTripDelete(object):

    def setUp(self):
        super(TestTripDelete, self).setUp()
        self.lt = LibTrips(self.server_url)
        self.srvcmd = ServerCmd(self.lt)

    def test_delete_trip_failure(self):
        id_unknown_trip = 9999999
        try:
            self.lt.delete_trip(id_unknown_trip)
        except RequestFailed, e:
            self.assertEquals(e.msg, "Gone")
            return
        self.fail()

    def test_delete_trip_success(self):
        id_trip_to_delete, _ = self.srvcmd.create_trip()
        try:
            self.lt.delete_trip(id_trip_to_delete)
        except RequestFailed, e:
            self.fail("Should succeed as this trip is supposed to exist")
        return # success


class TestTripUpdate(TestMother):
# class TestTripUpdate(object):

    def setUp(self):
        super(TestTripUpdate, self).setUp()
        self.lt = LibTrips(self.server_url)
        self.srvcmd = ServerCmd(self.lt)

        self.id_trip, _ = self.srvcmd.create_trip()

        self._register_teardown(lambda: self.srvcmd.delete_trip(self.id_trip))

    def test_update_trip_erroneous_parameters_should_succeed(self):
        dct = {'erroneous key': "erroneous value"}
        try:
            obj = self.lt.edit_trip(self.id_trip, **dct)
        except RequestFailed, e:
            self.fail("fail for request")
        except EditTripFormError, e:
            self.fail("fail for tripformerror")
        return # success

    def test_update_trip_valid_parameters_should_succeed(self):
        dct = {'interval_max': "5"}
        try:
            obj = self.lt.edit_trip(self.id_trip, **dct)
            self.assertEquals(obj.interval_max, 5)
        except RequestFailed, e:
            self.fail("fail for request")
        except EditTripFormError, e:
            self.fail("fail for tripformerror")
        return # success




if __name__ == "__main__":
    unittest.main()

# TODO:
# Test get/create/get/update/get/delete/get
#
# ../../../../bin/python test_trips.py
