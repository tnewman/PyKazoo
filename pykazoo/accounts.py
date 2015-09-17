class Accounts:
    """  2600hz Kazoo Accounts API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_account(self, account_id, filters=None):
        """ Get an Account

        :param account_id: ID of Account to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id), filters)

    def get_account_children(self, account_id, filters=None):
        """ Get the Children of an Account

        :param account_id: ID of Account to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/children', filters)

    def get_account_descendants(self, account_id, filters=None):
        """ Get the Descendants of an Account

        :param account_id: ID of Account to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/descendants', filters)

    def get_account_siblings(self, account_id, filters=None):
        """ Get the Siblings of an Account

        :param account_id: ID of Account to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     "/siblings", filters)

    def create_sub_account(self, parent_account_id, data):
        """ Create an Account

        :param parent_account_id: ID of Account parent.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type parent_account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(parent_account_id),
                                     data)

    def update_account(self, account_id, data):
        """ Updates an Account

        :param account_id: ID of Account.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id), data)

    def delete_account(self, account_id):
        """ Deletes an Account

        :param account_id: ID of Account.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id))
