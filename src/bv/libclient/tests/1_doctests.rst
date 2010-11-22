r"""

This script should be launched by a master process that control both bv.libclient and bv.server.

Do not forget to load the api_fixtures on the server side.
It contains a few users and a few trips already established.

You should reset your database and reload each time, and import the right settings
# export DJANGO_SETTINGS_MODULE=""
# bin/django-admin.py flush
# bin/django-admin.py loaddata cities.json
# bin/django-admin.py loaddata apitest.json # should contains the stuff


We are about to test a the api client against a real server, 
set up for testing purpose.


>>> real_server_url="http://127.0.0.1:8085" # no trailing slash !

Let's tests the trips:

>>> from bv.libclient import LibTrips
>>> lt = LibTrips(server_url=real_server_url)

>>> response = lt.count_trips()
>>> print response
0

>>> response = lt.list_trips()
>>> print response
[]


>>> city = lt.get_cities("Pari")

.. >>> print city.name, city.zipcode
.. Paris 75000



"""
