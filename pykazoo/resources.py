class Resources:
    """  2600hz Kazoo Resources API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_resources(self, account_id, filters):
        """ Get all Resources for an Account.

        :param account_id: ID of Account to get Resources for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/resources', filters)

    def get_resource(self, account_id, resource_id, filters):
        """ Get a specific Resources for an Account.

        :param account_id: ID of Account to get devices for.
        :param resource_id: ID of the Resource to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type resource_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/resources/' + str(resource_id), filters)

    def create_resource(self, account_id, data):
        """ Create a Resources

        :param account_id: ID of Account to create a Resource for.
        :param data: Kazoo Resource data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) +
                                     '/resources', data)

    def update_resource(self, account_id, resource_id, data):
        """ Updates a Device

        :param account_id: ID of Account to update Resource for.
        :param resource_id: ID of Resource to update.
        :param data: Kazoo Resource data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type resource_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/resources/' + str(resource_id), data)

    def delete_resource(self, account_id, resource_id):
        """ Deletes a Resource

        :param account_id: ID of Account to delete Resource from.
        :param resource_id: ID of Resource to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type resource_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/resources/' + str(resource_id))
