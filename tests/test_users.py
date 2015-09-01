import pykazoo.users
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec


class TestUsers(TestCase):
    def setUp(self):
        self.mock_rest_request = create_autospec(
            pykazoo.restrequest.RestRequest)

        self.users = pykazoo.users.Devices(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.user_id = '123123213rhh798ahf54hew4'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_users_request_call(self):
        self.users.get_users(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/users',
                                                      self.params)

    def test_get_users_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.users.get_users(self.account_id, self.params)
        assert return_data is self.data

    def test_get_user_request_call(self):
        self.users.get_user(self.account_id, self.user_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/users/' +
                                                      self.user_id,
                                                      self.params)

    def test_get_user_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.users.get_user(self.account_id, self.user_id,
                                          self.params)
        assert return_data is self.data

    def test_create_user_request_call(self):
        self.users.create_user(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/users',
                                                      self.data)

    def test_create_user_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.users.create_user(self.account_id, self.data)

        assert return_data is self.data

    def test_update_user_request_call(self):
        self.users.update_user(self.account_id, self.user_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/users/' +
                                                       self.user_id,
                                                       self.data)

    def test_update_user_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.users.update_user(self.account_id,
                                               self.user_id, self.data)

        assert return_data is self.data

    def test_delete_user_request_call(self):
        self.users.delete_user(self.account_id, self.user_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/users/' +
                                                         self.user_id)

    def test_delete_user_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.users.delete_user(self.account_id,
                                             self.user_id)

        assert return_data is self.data
