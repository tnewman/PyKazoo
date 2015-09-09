import pykazoo.menus
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestDevices(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.menus = pykazoo.menus.Menus(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.menu_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_menus_request_call(self):
        self.menus.get_menus(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/menus',
                                                      self.params)

    def test_get_menus_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.menus.get_menus(self.account_id, self.params)

        assert return_data is self.data

    def test_get_menu_request_call(self):
        self.menus.get_menu(self.account_id, self.menu_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/menus/' +
                                                      self.menu_id,
                                                      self.params)

    def test_get_menu_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.menus.get_menu(self.account_id, self.menu_id,
                                          self.params)

        assert return_data is self.data

    def test_create_menu_request_call(self):
        self.menus.create_menu(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/menus',
                                                      self.data)

    def test_create_menu_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.menus.create_menu(self.account_id, self.data)

        assert return_data is self.data

    def test_update_menu_request_call(self):
        self.menus.update_menu(self.account_id, self.menu_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/menus/' +
                                                       self.menu_id,
                                                       self.data)

    def test_update_menu_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.menus.update_menu(self.account_id, self.menu_id,
                                             self.data)

        assert return_data is self.data

    def test_delete_menu_request_call(self):
        self.menus.delete_menu(self.account_id, self.menu_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/menus/' +
                                                         self.menu_id)

    def test_delete_menu_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.menus.delete_menu(self.account_id, self.menu_id)

        assert return_data is self.data
