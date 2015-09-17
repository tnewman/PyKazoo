class Webhooks:
    """  2600hz Kazoo Webhooks API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_system_webhooks(self, filters=None):
        """ Get all Webhooks for the System.

        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('webhooks', filters)

    def get_webhooks(self, account_id, filters=None):
        """ Get all Webhooks for an Account.

        :param account_id: ID of Account to get Webhooks for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/webhooks', filters)

    def get_webhook(self, account_id, webhook_id, filters=None):
        """ Get a Webhook for an Account.

        :param account_id: ID of Account to get Webhook for.
        :param webhook_id: ID of Webhook to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type webhook_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/webhooks/' + str(webhook_id), filters)

    def create_webhook(self, account_id, data):
        """ Create a Webhook

        :param account_id: ID of Account to create Webhook for.
        :param data: Kazoo Device data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) +
                                     '/webhooks', data)

    def update_webhook(self, account_id, webhook_id, data):
        """ Updates a Webhook

        :param account_id: ID of Account to update Webhook for.
        :param webhook_id: ID of Webhook to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type webhook_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/webhooks/' + str(webhook_id), data)

    def delete_webhook(self, account_id, webhook_id):
        """ Delete a Webhook

        :param account_id: ID of Account to delete Webhook for.
        :param webhook_id: ID of Webhook to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type webhook_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/webhooks/' + str(webhook_id))
