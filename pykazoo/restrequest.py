import requests


class RestRequest:
    """ Makes a request to 2600hz Kazoo API using HTTP.

        :param api_url: The Kazoo API URL (ex: http://localhost:8000/v2).
        :param auth_token: The auth token to send in the header. Should be
            None if authentication is not used.
        :param rest_client: The module used to make requests.
        :type api_url: str, None
        :type auth_token: str, None
        :type rest_client: requests
    """

    def __init__(self, api_url, auth_token=None, rest_client=requests):
        self.api_url = api_url
        self.auth_token = auth_token
        self.rest_client = rest_client

    def get(self, action, params=None):
        """ Performs a Kazoo API GET request.

        :param action: The Kazoo API Action (example: /accounts/{id}).
        :param params: The query string parameters (example: filters).
        :return: Response Content
        :type action: str
        :type params: dict, None
        :rtype: dict
        """

        return self._request('GET', action, None, params)

    def put(self, action, data=None):
        """ Performs a Kazoo API PUT request.

        :param action: The Kazoo API Action (example: /accounts/{id}).
        :param data: The data to PUT.
        :return: Response Content
        :type action: str
        :type data: dict, None
        :rtype: dict
        """

        return self._request('PUT', action, data, None)

    def post(self, action, data=None):
        """ Performs a Kazoo API POST request.

        :param action: The Kazoo API Action (example: /accounts/{id}).
        :param data: The data to POST.
        :return: Response Content
        :type action: str
        :type data: dict, None
        :rtype: dict
        """

        return self._request('POST', action, data, None)

    def delete(self, action):
        """ Performs a Kazoo API DELETE request.

        :param action: The Kazoo API Action (example: /accounts/{id}).
        :return: Response Content
        :type action: str
        :rtype: dict
        """

        return self._request('DELETE', action, None, None)

    def _request(self, verb, action, data, params):
        """ Makes a request to the request client and validates the response.

        :param verb: HTTP Verb (GET, PUT, POST, DELETE).
        :param action: The Kazoo API Action (example: /accounts/{id}).
        :param data: The data to submit.
        :param params: The query string parameters (example: filters).
        :return: Response Content
        :type verb: str
        :type action: str
        :type data: dict, None
        :type params: dict, None
        :rtype: dict
        """

        self.headers = {'content-type': 'application/json'}

        if self.auth_token:
            self.headers['X-Auth-Token'] = self.auth_token

        url = str(self.api_url) + '/' + str(action)

        response = self.rest_client.request(verb, url, headers=self.headers,
                                            data=data, params=params)

        if response.status_code in [200, 201]:
            return response.json()
        else:
            message = 'Error Code: ' + str(response.status_code) + ' Data: ' \
                      + str(response.content)

            if response.status_code in [400, 404, 405, 415]:
                raise ValueError(message)
            elif response.status_code in [401]:
                raise PermissionError(message)
            elif response.status_code in [500, 503, 504]:
                raise ConnectionError(message)
            else:
                raise RuntimeError(message)
