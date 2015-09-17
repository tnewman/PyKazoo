class Media:
    """  2600hz Kazoo Media API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_all_media(self, account_id, filters=None):
        """ Get all Media for an Account.

        :param account_id: ID of Account to get devices for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/media', filters)

    def get_media(self, account_id, media_id, filters=None):
        """ Get Media for an Account.

        :param account_id: ID of Account to get devices for.
        :param media_id: ID of the Media to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type media_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/media/' + str(media_id), filters)

    def create_media(self, account_id, data):
        """ Create Media

        :param account_id: ID of Account to create Media for.
        :param data: Kazoo Media data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) +
                                     '/media', data)

    def update_media(self, account_id, media_id, data):
        """ Updates Media

        :param account_id: ID of Account to update Media for.
        :param media_id: ID of Media to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type media_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/media/' + str(media_id), data)

    def delete_media(self, account_id, media_id):
        """ Deletes Media

        :param account_id: ID of Account to delete Media from.
        :param media_id: ID of Device to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type media_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/media/' + str(media_id))

    def get_raw_media(self, account_id, media_id, filters=None):
        """ Get Raw Media for an Account.

        :param account_id: ID of Account to get devices for.
        :param media_id: ID of the Media to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type media_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/media/' + str(media_id) + '/raw',
                                     filters)

    def update_raw_media(self, account_id, media_id, data):
        """ Update Raw Media for an Account.

        :param account_id: ID of Account to get devices for.
        :param media_id: ID of the Media to get.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type media_id: str
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/media/' + str(media_id) + '/raw',
                                      data, 'application/x-base64')
