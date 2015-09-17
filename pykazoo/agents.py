class Agents:
    """  2600hz Kazoo Devices API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_agents(self, account_id, filters=None):
        """ Get all Agents for an Account.

        :param account_id: ID of Account to get Agents for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/agents', filters)

    def get_agent(self, account_id, agent_id, filters=None):
        """ Get a specific Devices for an Account.

        :param account_id: ID of Account to get Agent for.
        :param agent_id: ID of the Agent to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type agent_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/agents/' + str(agent_id), filters)

    def get_agents_stats(self, account_id, filters=None):
        """ Get Agent Stats for an Account.

        :param account_id: ID of Account to get Agent Stats for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/agents/stats', filters)
