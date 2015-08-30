from unittest import TestCase
from unittest.mock import Mock
from pykazoo.restrequest import RestRequest


class TestRestRequest(TestCase):
    def setUp(self):
        self.mock_requests = Mock()

        self.return_value_mock = Mock()
        self.return_value_mock.status_code = 200
        self.return_value_mock.content = 'Return Value Content'
        self.return_value_mock.json.return_value = {'data': 'data'}

        self.mock_requests.request.return_value = self.return_value_mock

        self.action = 'action'
        self.url = 'localhost'
        self.sample_data = {'test': 'data'}
        self.sample_params = {'test': 'param'}
        self.proper_url = self.url + '/' + self.action

        self.rest_request = RestRequest(self.url,
                                        rest_client=self.mock_requests)

        self.assert_mock_requests_called_with = \
            self.mock_requests.request.assert_called_with

    def test_get_sets_proper_request(self):
        self.rest_request.get(self.action, self.sample_params)
        self.assert_mock_requests_called_with('GET', self.proper_url,
                                              data=None,
                                              params=self.sample_params,
                                              headers={'content-type':
                                                       'application/json'})

    def test_put_sets_proper_request(self):
        self.rest_request.put(self.action, self.sample_data)
        self.assert_mock_requests_called_with('PUT', self.proper_url,
                                              data=self.sample_data,
                                              params=None,
                                              headers={'content-type':
                                                       'application/json'})

    def test_post_sets_proper_request(self):
        self.rest_request.post(self.action, self.sample_data)
        self.assert_mock_requests_called_with('POST', self.proper_url,
                                              data=self.sample_data,
                                              params=None,
                                              headers={'content-type':
                                                       'application/json'})

    def test_delete_sets_proper_request(self):
        self.rest_request.delete(self.action)
        self.assert_mock_requests_called_with('DELETE', self.proper_url,
                                              data=None, params=None,
                                              headers={'content-type':
                                                       'application/json'})

    def test_auth_token_header_when_auth_token_set(self):
        self.rest_request.auth_token = 'TOKEN'
        self.rest_request.delete(self.action)
        self.assert_mock_requests_called_with('DELETE', self.proper_url,
                                              data=None, params=None,
                                              headers={'content-type':
                                                       'application/json',
                                                       'X-Auth-Token':
                                                       'TOKEN'})

    def test_200_response_code_returns_json(self):
        self.return_value_mock.status_code = 200

        assert type(self.rest_request.delete(self.action)) is dict

    def test_201_response_code_returns_json(self):
        self.return_value_mock.status_code = 201

        assert type(self.rest_request.delete(self.action)) is dict

    def test_400_response_code_raises_value_error(self):
        self.return_value_mock.status_code = 400

        self.assertRaises(ValueError, self.rest_request.delete, self.action)

    def test_401_response_code_raises_permission_error(self):
        self.return_value_mock.status_code = 401

        self.assertRaises(PermissionError, self.rest_request.delete,
                          self.action)

    def test_404_response_code_raises_value_error(self):
        self.return_value_mock.status_code = 404

        self.assertRaises(ValueError, self.rest_request.delete, self.action)

    def test_415_response_code_raises_value_error(self):
        self.return_value_mock.status_code = 415

        self.assertRaises(ValueError, self.rest_request.delete, self.action)

    def test_500_response_code_raises_connection_error(self):
        self.return_value_mock.status_code = 500

        self.assertRaises(ConnectionError, self.rest_request.delete,
                          self.action)

    def test_503_response_code_raises_connection_error(self):
        self.return_value_mock.status_code = 503

        self.assertRaises(ConnectionError, self.rest_request.delete,
                          self.action)

    def test_504_response_code_raises_connection_error(self):
        self.return_value_mock.status_code = 504

        self.assertRaises(ConnectionError, self.rest_request.delete,
                          self.action)

    def test_other_response_code_raises_runtime_error(self):
        self.return_value_mock.status_code = 1234

        self.assertRaises(RuntimeError, self.rest_request.delete, self.action)
