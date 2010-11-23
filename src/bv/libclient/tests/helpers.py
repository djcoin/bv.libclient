import base64
from bv.libclient.baselib import BvResource


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

            import pdb;pdb.set_trace()
            return super(DummyLib, self).request(*args, **kwargs)

    return DummyLib

def get_basicauth_header(username, password):
    auth = base64.encodestring('%s:%s' % (username, password))[:-1]
    return { 'Authorization': 'Basic %s' % auth}

def get_authent_lib(username, password):
    return get_dummy_lib(get_basicauth_header(username,password))

