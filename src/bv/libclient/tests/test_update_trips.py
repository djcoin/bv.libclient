"""Test scenario:

Testing trips stuff

"""

import unittest
from bv.libclient.tests.helpers import TestMother
import bv.libclient.tests.helper_trip as helper_trip
from bv.libclient.tests.helper_trip import ServerCmd, get_valid_trip_full_data_v1

from bv.libclient.libtrips import LibTrips
from bv.libclient.exceptions import EditTripFormError

from restkit.errors import RequestFailed


# class TestTripUpdate(TestMother):
class TestTripUpdate(object):

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


class TestTripUpdateDemand(TestMother):
    """Demand specific tests"""
    pass

class TestTripUpdateDemandOnlyOne(TestMother):
    """Massive test to update each demand field with valid data"""


    def setUp(self):
        super(TestTripUpdateDemandOnlyOne, self).setUp()
        self.lt = LibTrips(self.server_url)
        self.srvcmd = ServerCmd(self.lt)

        # be sure to not supply
        self.updates_data = get_valid_trip_full_data_v1()
        self.id_trip, _ = self.srvcmd.create_trip()

        self._register_teardown(lambda: self.srvcmd.delete_trip(self.id_trip))


    def test_all_valid_updates(self):
        """This test will test extensively all updates fields possible with valid data.
        Will stop at first failure.
        Remember that we are updating the same trip that's being built only once.
        """

        # the alert case is to be treated somewhere else
        del self.updates_data['alert']

        for k, v in self.updates_data.iteritems():
            try:
                # try updates one by one
                obj = self.lt.edit_trip(self.id_trip, **{k: v})
                # TODO: check that the data has been updated
                # self.assertEquals(getattr(obj, k), v)
                print obj
            except RequestFailed, e:
                print "Exception for %s = %s" % (k, v)
                self.fail("fail for request")
            except EditTripFormError, e:
                print "Exception for %s = %s" % (k, v)
                self.fail("fail for tripformerror")
            # except Exception, e: # could be another exception ?!
            #     print "Exception for %s = %s" % (k, v)
            #     raise e
                # import pdb; pdb.set_trace()
                # self.fail()

    def test_alert(self):

        alert_update = self.updates_data['alert']
        msg = self.lt.set_alert(self.id_trip, alert_update)
        self.assertEquals('OK', msg.body_string())

    # TODO
    def test_all_not_valid_updates(self):
        """Check that for each erroneous data, a failure will ensue."""
        pass


class TestTripUpdateOffer(TestMother):
    """Offer specific tests"""
    pass

class TestTripUpdateOfferOnlyOne(TestMother):
    pass

"""
Valid parameters for creation AND updates::

    * `departure_city`: the trip departure city  (*required*)
    * `departure_address`: the trip departure adress
    * `departure_point`: the departure geographical point for the trip (*required*)
    * `arrival_city`: the trip arrival city
    * `arrival_address`: the trip arrival adress (*required*)
    * `arrival_point`: the arrival geographical point for the trip (*required*)
    * `regular`: Is the trip a regular one ? True = Yes (*required*)
    * `date`: the date of the trip (*required*)
    * `interval_min`: nomber of interval (days) accepted before the departure date
    * `interval_max`: nomber of interval (days) accepted after the departure date
    * `dows`: if the trip i a regular one, dows contains a Json array containing days of weeks. (*required if the trip is regular*)
    * `comment`: an optionnal comment for this trip
    * `demand`: True or False
    * `offer`: True or False
    * `demand_radius`: perimeter of the passenger search
    * `demand_smokers_accepted`: weather the passenger accepts smokers or not
    * `demand_pets_accepted`: weather the passenger accepts pets or not
    * `demand_place_for_luggage`:  weather the passenger need place for laggages or not
    * `demand_car_type`: the car type id asked by the passenger
    * `demand_min_remaining_seats`:  the number of remaining seats for the passenger
    * `demand_max_km_price`: Maximum price per KM
    * `offer_radius`: perimeter of the conductor search
    * `offer_checkpoints`: checkpoints of the offer trip
    * `offer_route`: SIG route
    * `offer_km_price`: Price per KM asked by the driver
    * `offer_radius`: perimeter of the passenger search
    * `offer_smokers_accepted`: weather the passenger accepts smokers or not
    * `offer_pets_accepted`: weather the passenger accepts pets or not
    * `offer_place_for_luggage`:  weather the driver have place for laggages or not
    * `offer_car_type`: the car type the driver have
    * `offer_seats_available`:  the number of remaining seats for the driver

(only for creation?!)
    * `tag`: a free to use tag. If specified, all trip must have it
"""


if __name__ == "__main__":
    unittest.main()

# TODO:
# Test get/create/get/update/get/delete/get
#
# ../../../../bin/python test_trips.py
