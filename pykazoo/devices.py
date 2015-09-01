class Devices:
    """  2600hz Kazoo Devices API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_devices(self, account_id, filters):
        """ Get all Devices for an Account.

        :param account_id: ID of Account to get devices for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/devices', filters)

    def get_device(self, account_id, device_id, filters):
        """ Get a specific Devices for an Account.

        :param account_id: ID of Account to get devices for.
        :param device_id: ID of the Device to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/devices/' + str(device_id), filters)

    def create_device(self, account_id, data):
        """ Create a Device

        :param account_id: ID of Account to create device for.
        :param data: Kazoo Device data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + account_id + '/devices',
                                     data)

    def update_device(self, account_id, device_id, data):
        """ Updates a Device

        :param account_id: ID of Account to update device for.
        :param device_id: ID of Device to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type device_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/devices/' + str(device_id), data)

    def delete_device(self, account_id, device_id):
        """ Deletes a Device

        :param account_id: ID of Account to delete device from.
        :param device_id: ID of Device to delete.
        :return: Kazoo Data (see official API docs).
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + account_id +
                                        '/devices/' + device_id)
