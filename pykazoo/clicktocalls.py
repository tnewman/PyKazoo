class ClickToCalls:
    """  2600hz Kazoo Click to Call API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_click_to_calls(self, account_id, filters=None):
        """ Get all Click to Calls for an Account.

        :param account_id: ID of Account to get Click to Calls for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/clicktocall', filters)

    def get_click_to_call(self, account_id, click_to_call_id, filters=None):
        """ Get a specific Click to Call for an Account.

        :param account_id: ID of Account to get Click to Calls for.
        :param click_to_call_id: ID of the Click to Call to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type click_to_call_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/clicktocall/' + str(click_to_call_id),
                                     filters)

    def create_click_to_call(self, account_id, data):
        """ Create a Click to Call

        :param account_id: ID of Account to create Click to Call for.
        :param data: Kazoo Click to Call data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) +
                                     '/clicktocall', data)

    def update_click_to_call(self, account_id, click_to_call_id, data):
        """ Updates a Click to Call

        :param account_id: ID of Account to update Click to Call for.
        :param click_to_call_id: ID of Click to Call to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type click_to_call_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/clicktocall/' + str(click_to_call_id),
                                      data)

    def delete_click_to_call(self, account_id, click_to_call_id):
        """ Deletes a Click to Call

        :param account_id: ID of Account to delete Click to Call from.
        :param click_to_call_id: ID of Click to Call to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type click_to_call_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/clicktocall/' +
                                        str(click_to_call_id))

    def connect_click_to_call(self, account_id, click_to_call_id,
                              filters=None):
        """ Connects a Click to Call

        :param account_id: ID of Account to connect Click to Call for.
        :param click_to_call_id: ID of Click to Call to connect.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/clicktocall/' +
                                      str(click_to_call_id) + '/connect',
                                      filters)

    def get_click_to_call_history(self, account_id, click_to_call_id,
                                  filters=None):
        """ Gets history for a  Click to Call

        :param account_id: ID of Account to get Click to Call history for.
        :param click_to_call_id: ID of Click to Call to get history for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/clicktocall/' + str(click_to_call_id) +
                                     '/history', filters)
