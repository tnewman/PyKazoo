class Conferences:
    """  2600hz Kazoo Conferences API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_conferences(self, account_id, filters=None):
        """ Get all Conferences for an Account.

        :param account_id: ID of Account to get Conferences for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/conferences', filters)

    def get_conference(self, account_id, conference_id, filters=None):
        """ Get a specific Conference for an Account.

        :param account_id: ID of Account to get Conferences for.
        :param conference_id: ID of the Conference to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type conference_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/conferences/' + str(conference_id),
                                     filters)

    def create_conference(self, conference_id, data):
        """ Create a Conference

        :param conference_id: ID of Account to create Conference for.
        :param data: Kazoo Directory data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type conference_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(conference_id) +
                                     '/conferences', data)

    def update_conference(self, account_id, conference_id, data):
        """ Updates a Conference

        :param account_id: ID of Account to update Conference for.
        :param conference_id: ID of Conference to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type conference_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/conferences/' + str(conference_id),
                                      data)

    def delete_conference(self, account_id, conference_id):
        """ Deletes a Timed Route

        :param account_id: ID of Account to delete Timed Route from.
        :param conference_id: ID of Conference to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type conference_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/conferences/' + str(conference_id))
