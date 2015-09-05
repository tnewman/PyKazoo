class Callflows:
    """  2600hz Kazoo Callflows API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_callflows(self, account_id, filters):
        """ Get all Callflows for an Account.

        :param account_id: ID of Account to get Callflows for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/callflows', filters)

    def get_callflow(self, account_id, callflow_id, filters):
        """ Get a specific Callflows for an Account.

        :param account_id: ID of Account to get devices for.
        :param callflow_id: ID of the Callflow to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type callflow_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/callflows/' + str(callflow_id), filters)

    def create_callflow(self, account_id, data):
        """ Create a Callflow

        :param account_id: ID of Account to create Callflow for.
        :param data: Kazoo Callflow data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) +
                                     '/callflows', data)

    def update_callflow(self, account_id, callflow_id, data):
        """ Updates a Callflow

        :param account_id: ID of Account to update device for.
        :param callflow_id: ID of Callflow to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type callflow_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/callflows/' + str(callflow_id), data)

    def delete_callflow(self, account_id, callflow_id):
        """ Deletes a Callflow

        :param account_id: ID of Callflow to delete device from.
        :param callflow_id: ID of Callflow to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type callflow_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/callflows/' + str(callflow_id))
