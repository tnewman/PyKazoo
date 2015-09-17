class Users:
    """  2600hz Kazoo Users API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_users(self, account_id, filters=None):
        """ Get all Users for an Account.

        :param account_id: ID of Account to get Users for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/users', filters)

    def get_user(self, account_id, user_id, filters=None):
        """ Get a specific User for an Account.

        :param account_id: ID of Account to get User for.
        :param user_id: ID of the User to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type user_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/users/' + str(user_id), filters)

    def create_user(self, account_id, data):
        """ Create a User

        :param account_id: ID of Account to create User for.
        :param data: Kazoo User data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) + '/users',
                                     data)

    def update_user(self, account_id, user_id, data):
        """ Updates a User

        :param account_id: ID of Account to update User for.
        :param user_id: ID of User to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type user_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/users/' + str(user_id), data)

    def delete_user(self, account_id, user_id):
        """ Deletes a User

        :param account_id: ID of Account to delete User from.
        :param user_id: ID of User to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type user_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/users/' + str(user_id))
