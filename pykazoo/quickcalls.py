class QuickCalls:
    """  2600hz Kazoo Quick Call API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def quick_call_device(self, account_id, device_id, phone_number,
                          filters=None):
        """ Perform a Quick Call for a Device.

        :param account_id: ID of Account for Quick Call.
        :param device_id: ID of Device for Quick Call.
        :param phone_number: Phone Number to Quick Call.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/devices/' + str(device_id) +
                                     '/quickcall/' + str(phone_number),
                                     filters)

    def quick_call_user(self, account_id, user_id, phone_number, filters=None):
        """ Perform a Quick Call for a User.

        :param account_id: ID of Account to get Click to Calls for.
        :param user_id: ID of User for Quick Call.
        :param phone_number: Phone Number to Quick Call.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type user_id: str
        :type filters: dict, None
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/users/' + str(user_id) +
                                     '/quickcall/' + str(phone_number),
                                     filters)
