import pykazoo.clicktocalls
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestDevices(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.click_to_calls = pykazoo.clicktocalls.ClickToCalls(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.click_to_call_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_click_to_calls_request_call(self):
        self.click_to_calls.get_click_to_calls(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/clicktocall',
                                                      self.params)

    def test_get_click_to_calls_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.click_to_calls.get_click_to_calls(self.account_id,
                                                             self.params)

        assert return_data is self.data

    def test_get_click_to_call_request_call(self):
        self.click_to_calls.get_click_to_call(self.account_id,
                                              self.click_to_call_id,
                                              self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/clicktocall/' +
                                                      self.click_to_call_id,
                                                      self.params)

    def test_get_click_to_call_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.click_to_calls.get_click_to_call(
            self.account_id, self.click_to_call_id, self.params)

        assert return_data is self.data

    def test_create_click_to_call_request_call(self):
        self.click_to_calls.create_click_to_call(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/clicktocall',
                                                      self.data)

    def test_create_device_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.click_to_calls.create_click_to_call(self.account_id,
                                                               self.data)

        assert return_data is self.data

    def test_update_click_to_call_request_call(self):
        self.click_to_calls.update_click_to_call(self.account_id,
                                                 self.click_to_call_id,
                                                 self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/clicktocall/' +
                                                       self.click_to_call_id,
                                                       self.data)

    def test_update_click_to_call_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.click_to_calls.update_click_to_call(
            self.account_id, self.click_to_call_id, self.data)

        assert return_data is self.data

    def test_delete_click_to_call_request_call(self):
        self.click_to_calls.delete_click_to_call(self.account_id,
                                                 self.click_to_call_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/clicktocall/' +
                                                         self.click_to_call_id)

    def test_delete_click_to_call_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.click_to_calls.delete_click_to_call(
            self.account_id, self.click_to_call_id)

        assert return_data is self.data

    def test_connect_click_to_call_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.click_to_calls.connect_click_to_call(
            self.account_id, self.click_to_call_id, self.params)

        assert return_data is self.data

    def test_connect_click_to_call_call(self):
        self.click_to_calls.connect_click_to_call(self.account_id,
                                                  self.click_to_call_id,
                                                  self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/clicktocall/' +
                                                       self.click_to_call_id +
                                                       '/connect', self.data)

    def test_get_click_to_call_history_returns_dict(self):
        self.mock_rest_request.get.return_value = self.params
        return_data = self.click_to_calls.get_click_to_call_history(
            self.account_id, self.click_to_call_id, self.params)

        assert return_data is self.params

    def test_get_click_to_call_history_call(self):
        self.click_to_calls.get_click_to_call_history(self.account_id,
                                                      self.click_to_call_id,
                                                      self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/clicktocall/' +
                                                      self.click_to_call_id +
                                                      '/history', self.params)
