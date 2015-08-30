from unittest import TestCase
from unittest.mock import Mock
from pykazoo.restrequest import RestRequest


class TestRestRequest(TestCase):
    def setUp(self):
        self.mock_requests = Mock()
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
