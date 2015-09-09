class Directories:
    """  2600hz Kazoo Directories API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_directories(self, account_id, filters):
        """ Get all Devices for an Account.

        :param account_id: ID of Account to get Directories for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/directories', filters)

    def get_directory(self, account_id, directory_id, filters):
        """ Get a specific Devices for an Account.

        :param account_id: ID of Account to get Directory for.
        :param directory_id: ID of the Directory to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type directory_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/directories/' + str(directory_id),
                                     filters)

    def create_directory(self, account_id, data):
        """ Create a Directory

        :param account_id: ID of Account to create Directory for.
        :param data: Kazoo Directory data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) +
                                     '/directories', data)

    def update_directory(self, account_id, directory_id, data):
        """ Updates a Directory

        :param account_id: ID of Account to update Directory for.
        :param directory_id: ID of Directory to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type directory_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/directories/' + str(directory_id),
                                      data)

    def delete_directory(self, account_id, directory_id):
        """ Deletes a Device

        :param account_id: ID of Account to delete Directory from.
        :param directory_id: ID of Directory to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type directory_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/directories/' + str(directory_id))
