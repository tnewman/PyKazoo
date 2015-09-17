class Queues:
    """  2600hz Kazoo Queues API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_queues(self, account_id, filters=None):
        """ Get all Queues for an Account.

        :param account_id: ID of Account to get Queues for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/queues', filters)

    def get_queue(self, account_id, queue_id, filters=None):
        """ Get a specific Queue for an Account.

        :param account_id: ID of Account to get Queues for.
        :param queue_id: ID of the Queue to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type queue_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/queues/' + str(queue_id), filters)

    def create_queue(self, account_id, data):
        """ Create a Queue

        :param account_id: ID of Account to create device for.
        :param data: Kazoo Device data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) +
                                     '/queues', data)

    def update_queue(self, account_id, queue_id, data):
        """ Updates a Queue

        :param account_id: ID of Account to update Queue for.
        :param queue_id: ID of Queue to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type queue_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/queues/' + str(queue_id), data)

    def delete_queue(self, account_id, queue_id):
        """ Deletes a Queue

        :param account_id: ID of Account to delete Queue from.
        :param queue_id: ID of Queue to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type queue_id: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/queues/' + str(queue_id))

    def get_queues_stats(self, account_id, filters=None):
        """ Gets Devices Status

        :param account_id: ID of Account to get Queues stats for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/queues/stats', filters)
