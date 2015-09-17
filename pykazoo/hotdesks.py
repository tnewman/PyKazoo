class Hotdesks:
    """  2600hz Kazoo Hotdesks API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_hotdesks(self, account_id, filters=None):
        """ Get all Hotdesks for an Account.

        :param account_id: ID of Account to get Hotdesks for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/users/hotdesks', filters)

    def get_hotdesk(self, account_id, user_id, filters=None):
        """ Get a User's Hotdesk for an Account.

        :param account_id: ID of Account to get Hotdesk for.
        :param user_id: ID of the User to get Hotdesk for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type user_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/users/' + str(user_id) + '/hotdesks',
                                     filters)

    def create_hotdesk(self, account_id, user_id, data):
        """ Create a User's Hotdesk

        :param account_id: ID of Account to create Hotdesk for.
        :param user_id: ID of User to create Hotdesk for.
        :param data: Kazoo Device data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type user_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) +
                                     '/users/' + str(user_id) + '/hotdesks',
                                     data)

    def update_hotdesk(self, account_id, user_id, data):
        """ Updates a User's Hotdesk

        :param account_id: ID of Account to update Hotdesk for.
        :param user_id: ID of Update to create Hotdesk for.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type user_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/users/' + str(user_id) + '/hotdesks',
                                      data)

    def delete_hotdesk(self, account_id, user_id):
        """ Deletes a User's Hotdesk

        :param account_id: ID of Account to delete Hotdesk from.
        :param user_id: ID of User to delete Hotdesk for.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type user_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/users/' + str(user_id) + '/hotdesks')
