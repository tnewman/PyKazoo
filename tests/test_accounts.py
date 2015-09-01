import pykazoo.accounts
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec


class TestAccounts(TestCase):
    def setUp(self):
        self.mock_rest_request = create_autospec(
            pykazoo.restrequest.RestRequest)

        self.accounts = pykazoo.accounts.Accounts(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_account_request_call(self):
        self.accounts.get_account(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id,
                                                      self.params)

    def test_get_account_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.accounts.get_account(self.account_id, self.params)

        assert return_data is self.data

    def test_get_account_children_request_call(self):
        self.accounts.get_account_children(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/children',
                                                      self.params)

    def test_get_account_children_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.accounts.get_account_children(self.account_id,
                                                         self.params)
        assert return_data is self.data

    def test_get_account_descendants_request_call(self):
        self.accounts.get_account_descendants(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/descendants',
                                                      self.params)

    def test_get_account_descendants_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.accounts.get_account_descendants(self.account_id,
                                                            self.params)
        assert return_data is self.data

    def test_get_account_siblings_request_call(self):
        self.accounts.get_account_siblings(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/siblings',
                                                      self.params)

    def test_get_account_siblings_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.accounts.get_account_siblings(self.account_id,
                                                         self.params)
        assert return_data is self.data

    def test_create_sub_account_request_call(self):
        self.accounts.create_sub_account(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id,
                                                      self.data)

    def test_create_sub_account_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.accounts.create_sub_account(self.account_id,
                                                       self.data)

        assert return_data is self.data

    def test_update_account_request_call(self):
        self.accounts.update_account(self.account_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id,
                                                       self.data)

    def test_update_account_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.accounts.update_account(self.account_id,
                                                   self.data)

        assert return_data is self.data

    def test_delete_account_request_call(self):
        self.accounts.delete_account(self.account_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id)

    def test_delete_account_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.accounts.delete_account(self.account_id)

        assert return_data is self.data
