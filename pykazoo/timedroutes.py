class TimedRoutes:
    """  2600hz Kazoo Timed Routes API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_timed_routes(self, account_id, filters=None):
        """ Get all Timed Routes for an Account.

        :param account_id: ID of Account to get Timed Routes for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/temporal_rules', filters)

    def get_timed_route(self, account_id, timed_route_id, filters=None):
        """ Get a specific Timed Route for an Account.

        :param account_id: ID of Account to get Directory for.
        :param timed_route_id: ID of the Timed Route to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type timed_route_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/temporal_rules/' + str(timed_route_id),
                                     filters)

    def create_timed_route(self, account_id, data):
        """ Create a Timed Route

        :param account_id: ID of Account to create Timed Route for.
        :param data: Kazoo Directory data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) +
                                     '/temporal_rules', data)

    def update_timed_route(self, account_id, timed_route_id, data):
        """ Updates a Timed Route

        :param account_id: ID of Account to update Timed Route for.
        :param timed_route_id: ID of Timed Route to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type timed_route_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/temporal_rules/' + str(timed_route_id),
                                      data)

    def delete_timed_route(self, account_id, timed_route_id):
        """ Deletes a Timed Route

        :param account_id: ID of Account to delete Timed Route from.
        :param timed_route_id: ID of Timed Route to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type timed_route_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/temporal_rules/' +
                                        str(timed_route_id))
