import requests


class RestRequest:
    def __init__(self, api_url, auth_token=None, rest_client=requests):
        self.api_url = api_url
        self.auth_token = auth_token
        self.rest_client = rest_client

    def get(self, action, params=None):
        return self._request('GET', action, None, params)

    def put(self, action, data=None):
        return self._request('PUT', action, data, None)

    def post(self, action, data=None):
        return self._request('POST', action, data, None)

    def delete(self, action):
        return self._request('DELETE', action, None, None)

    def _request(self, verb, action, data, params):
        self.headers = {'content-type': 'application/json'}

        if self.auth_token:
            self.headers['X-Auth-Token'] = self.auth_token

        url = str(self.api_url) + '/' + str(action)

        response = self.rest_client.request(verb, url, headers=self.headers,
                                            data=data, params=params)

        if response.status_code in [200, 201]:
            return response.json()
        else:
            message = 'Error Code: ' + str(response.status_code) + ' Data: ' + \
                      str(response.content)

            if response.status_code in [400, 404, 415]:
                raise ValueError(message)
            elif response.status_code in [401]:
                raise PermissionError(message)
            elif response.status_code in [500, 503, 504]:
                raise ConnectionError(message)
            else:
                raise RuntimeError(message)
