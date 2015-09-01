import pykazoo.restrequest


class PyKazooClient:
    def __init__(self, rest_request=pykazoo.restrequest):
        self._rest_request = rest_request
