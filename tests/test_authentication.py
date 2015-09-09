import hashlib
import pykazoo.authentication
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestAuthentication(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.authentication = pykazoo.authentication.Authentication(
            self.mock_rest_request)

        self.token = 'SAMPLE_TOKEN'

    def test_api_auth_request_call(self):
        self.authentication.api_auth('SAMPLE_API_KEY')
        data = {'data': {'api_key': 'SAMPLE_API_KEY'}}
        self.mock_rest_request.put.assert_called_with('api_auth', data)

    def test_api_auth_returns_dict(self):
        data = {'auth_token': 'TOKEN'}
        self.mock_rest_request.put.return_value = data

        return_data = self.authentication.api_auth('SAMPLE_API_KEY')

        assert data is return_data

    def test_api_auth_sets_auth_token(self):
        data = {'auth_token': 'TOKEN'}
        self.mock_rest_request.put.return_value = data

        self.authentication.api_auth('SAMPLE_API_KEY')

        assert self.mock_rest_request.auth_token is data['auth_token']

    def test_user_auth_request_call(self):
        self.authentication.user_auth('USER', 'PASSWORD', 'ACCOUNT')

        combined_encoded = ('USER' + ':' + 'PASSWORD').encode('utf-8')
        md5_user_pass = hashlib.md5(combined_encoded).hexdigest()
        data = {'data': {'credentials': md5_user_pass,
                         'account_name': 'ACCOUNT'}}

        self.mock_rest_request.put.assert_called_with('user_auth', data)

    def test_user_auth_returns_dict(self):
        data = {'auth_token': 'TOKEN'}
        self.mock_rest_request.put.return_value = data

        return_data = self.authentication.user_auth('USER', 'PASS', 'ACCOUNT')

        assert data is return_data

    def test_user_auth_sets_auth_token(self):
        data = {'auth_token': 'TOKEN'}
        self.mock_rest_request.put.return_value = data

        self.authentication.user_auth('USER', 'PASS', 'ACCOUNT')

        assert self.mock_rest_request.auth_token is data['auth_token']
