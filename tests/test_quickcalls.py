import pykazoo.restrequest
import pykazoo.quickcalls
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestQuickCalls(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.quick_calls = pykazoo.quickcalls.QuickCalls(
            self.mock_rest_request)
        self.params = {'test': 'params'}
        self.data = {'test': 'data'}
        self.account_id = 'jojfj0ajfwjeipfjio54'
        self.device_id = 'jojifewjfojiewaofj'
        self.user_id = '23432423rewajojio'
        self.phone_number = 15555555555

    def test_quick_call_device_request_call(self):
        self.quick_calls.quick_call_device(self.account_id, self.device_id,
                                           self.phone_number, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/devices/' +
                                                      self.device_id +
                                                      '/quickcall/' +
                                                      str(self.phone_number),
                                                      self.params)

    def test_quick_call_device_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.quick_calls.quick_call_device(self.account_id,
                                                         self.device_id,
                                                         self.phone_number,
                                                         self.params)

        assert return_data is self.data

    def test_quick_call_user_request_call(self):
        self.quick_calls.quick_call_user(self.account_id, self.device_id,
                                         self.phone_number, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/users/' +
                                                      self.device_id +
                                                      '/quickcall/' +
                                                      str(self.phone_number),
                                                      self.params)

    def test_quick_call_user_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.quick_calls.quick_call_user(self.account_id,
                                                       self.user_id,
                                                       self.phone_number,
                                                       self.params)

        assert return_data is self.data
