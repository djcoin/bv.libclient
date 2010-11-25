# form that validate this api
# /home/sim/minitage/django/bv.server/src/bv/server/carpool/forms.py:289

# Convention defined troughout the project (client and server)
TRIP_OFFER = 0
TRIP_DEMAND = 1
TRIP_BOTH = 2


class ServerCmd(object):

    def __init__(self, libtrip):
        self.lt = libtrip

## FIXME: server_create_trip and server_delete_trip are created using the api.
##        should be better by erasing/loading specific fixtures

# TODO: create offer/demand
    def create_trip(self):
        """set up method:
            return a trip that was created on the server side without risk"""
        print "Fixture: creating valid trip"
        trip = self.lt.add_trip(**get_valid_trip_full_data())
        return (trip.id, trip)

    def delete_trip(self, id_trip):
        print "Fixture: deleting valid trip"
        self.lt.delete_trip(id_trip)


def get_valid_trip_full_data():
    """return all the data that can be obtain to define a valid trip.
    """
    return {
    'trip_type': "%d" % TRIP_DEMAND,
    'departure_address': "",
    'departure_city': "toulouse",
    'departure_point': "POINT(1.4429513 43.60436300000001)",
    'arrival_city': "paris",
    'arrival_point': "POINT(2.3509871 48.85666670000002)",
    'comment': "",
    'date': "20/01/2010",
    'demand-passenger_car_type': "",
    'demand-passenger_max_km_price': "",
    'demand-passenger_min_remaining_seats': "",
    'demand-passenger_pets_accepted': "on",
    'demand-passenger_smokers_accepted': "on",
    'demand-radius': "500",
    'interval_max': "0",
    'interval_min': "7",
    'name': "announce name",
    'offer-radius': "500",
    'regular': "False",
    'time': "8",
    'alert': "on",
    }


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
