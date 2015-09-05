class PhoneNumbers:
    """  2600hz Kazoo PhoneNumbers API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_phone_numbers(self, account_id, filters):
        """ Get all Phone Numbers for an Account.

        :param account_id: ID of Account to get Phone Numbers for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/phone_numbers', filters)

    def get_phone_number(self, account_id, phone_number, filters):
        """ Get a specific Phone Number for an Account.

        :param account_id: ID of Account to get Phone Number for.
        :param phone_number: ID of the Phone Number to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type phone_number: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/phone_numbers/' + str(phone_number),
                                     filters)

    def create_phone_number(self, account_id, phone_number, data):
        """ Create a Phone Number

        :param account_id: ID of Account to create device for.
        :param phone_number: Phone Number to create.
        :param data: Kazoo Device data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type phone_number: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) +
                                     '/phone_numbers/' + str(phone_number),
                                     data)

    def update_phone_number(self, account_id, phone_number, data):
        """ Updates a Phone Number

        :param account_id: ID of Account to update device for.
        :param phone_number: ID of Phone Number to update.
        :param data: Kazoo Account data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type phone_number: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/phone_numbers/' + str(phone_number),
                                      data)

    def delete_phone_number(self, account_id, phone_number):
        """ Deletes a Device

        :param account_id: ID of Account to delete device from.
        :param phone_number: Phone Number to delete.
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type phone_number: str
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/phone_numbers/' + str(phone_number))
