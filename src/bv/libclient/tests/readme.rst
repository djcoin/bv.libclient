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
"""
