import base64
import unittest

from bv.libclient.baselib import BvResource, BaseLib

class TestMother(unittest.TestCase):
    def setUp(self):
        BaseLib._resource_class = get_authent_lib('toto', 'tototo')
        # real test server url - no trailing slash ! -
        self.server_url = "http://127.0.0.1:8085"
        self._teardown = []
        self._register_teardown = lambda x: self._teardown.append(x)

    def tearDown(self):
        # teardown
        while len(self._teardown):
            self._teardown.pop()()

        # WARNING SHOULD BE LAST THING TO tearDown
        BaseLib._resource_class = BvResource


def get_dummy_lib(header):

    class DummyLib(BvResource):

        def __init__(self, *args, **kwargs):
            self.header = header
            super(DummyLib, self).__init__(*args, **kwargs)

        def request(self, *args, **kwargs):
            if kwargs:
                new_headers = self.header
                headers = kwargs.get('headers',{})
                if headers:
                    new_headers.update(headers)
                kwargs['headers'] = new_headers

            return super(DummyLib, self).request(*args, **kwargs)

    return DummyLib

def get_basicauth_header(username, password):
    auth = base64.encodestring('%s:%s' % (username, password))[:-1]
    return { 'Authorization': 'Basic %s' % auth}

def get_authent_lib(username, password):
    return get_dummy_lib(get_basicauth_header(username,password))


