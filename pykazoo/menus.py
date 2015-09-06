class Menus:
    """  2600hz Kazoo Menus API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_menus(self, account_id, filters):
        """ Get all Menus for an Account.

        :param account_id: ID of Account to get menus for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/menus', filters)

    def get_menu(self, account_id, menu_id, filters):
        """ Get a specific Menu for an Account.

        :param account_id: ID of Account to get a menu for.
        :param menu_id: ID of the Menu to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type menu_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/menus/' + str(menu_id), filters)

    def create_menu(self, menu_id, data):
        """ Create a Menu

        :param menu_id: ID of Account to create a menu for.
        :param data: Kazoo Device data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type menu_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(menu_id) +
                                     '/menus', data)

    def update_menu(self, account_id, menu_id, data):
        """ Updates a Menu

        :param account_id: ID of Account to update Menu for.
        :param menu_id: ID of Menu to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type menu_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/menus/' + str(menu_id), data)

    def delete_menu(self, account_id, menu_id):
        """ Deletes a Menu

        :param account_id: ID of Account to delete device from.
        :param menu_id: ID of Menu to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type menu_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/menus/' + str(menu_id))
