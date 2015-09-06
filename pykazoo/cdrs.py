class CDRs:
    """  2600hz Kazoo CDRs API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_cdrs(self, filters):
        """ Get all CDRs.

        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('cdrs', filters)
