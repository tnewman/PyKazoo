class Faxes:
    """  2600hz Kazoo Menus API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_faxes(self, account_id, filters):
        """ Get all Outgoing Faxes for an Account.

        :param account_id: ID of Account to get menus for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/faxes/outgoing', filters)

    def create_fax(self, account_id, data):
        """ Send an Outgoing Fax

        :param account_id: ID of Account to create an Outgoing Fax for.
        :param data: Kazoo Device data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) +
                                     '/faxes/outgoing', data)
