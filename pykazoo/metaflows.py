class Metaflows:
    """  2600hz Kazoo Metaflows API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_account_metaflows(self, account_id):
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/metaflows', None)

    def get_callflow_metaflows(self, account_id, callflow_id):
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/callflows/' + str(callflow_id) +
                                     '/metaflows', None)

    def get_device_metaflows(self, account_id, device_id):
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/devices/' + str(device_id) +
                                     '/metaflows', None)

    def update_account_metaflows(self, account_id, data):
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/metaflows', data)

    def update_callflow_metaflows(self, account_id, callflow_id, data):
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/callflows/' + str(callflow_id) +
                                      '/metaflows', data)

    def update_device_metaflows(self, account_id, device_id, data):
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/devices/' + str(device_id) +
                                      '/metaflows', data)

    def delete_account_metaflows(self, account_id):
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/metaflows')

    def delete_callflow_metaflows(self, account_id, callflow_id):
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/callflows/' + str(callflow_id) +
                                        '/metaflows')

    def delete_device_metaflows(self, account_id, device_id):
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/devices/' + str(device_id) +
                                        '/metaflows')
