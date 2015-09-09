import pykazoo.restrequest
import pykazoo.phonenumbers
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestPhoneNumbers(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.phone_numbers = pykazoo.phonenumbers.PhoneNumbers(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.phone_number = '+15555555555'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_phone_numbers_request_call(self):
        self.phone_numbers.get_phone_numbers(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/phone_numbers',
                                                      self.params)

    def test_get_phone_numbers_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.phone_numbers.get_phone_numbers(self.account_id,
                                                           self.params)

        assert return_data is self.data

    def test_get_phone_number_request_call(self):
        self.phone_numbers.get_phone_number(self.account_id, self.phone_number,
                                            self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/phone_numbers/' +
                                                      self.phone_number,
                                                      self.params)

    def test_get_phone_number_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.phone_numbers.get_phone_number(self.account_id,
                                                          self.phone_number,
                                                          self.params)

        assert return_data is self.data

    def test_create_phone_numbers_request_call(self):
        self.phone_numbers.create_phone_number(self.account_id,
                                               self.phone_number,
                                               self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/phone_numbers/' +
                                                      str(self.phone_number),
                                                      self.data)

    def test_create_phone_numbers_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.phone_numbers.create_phone_number(self.account_id,
                                                             self.phone_number,
                                                             self.data)

        assert return_data is self.data

    def test_update_phone_numbers_request_call(self):
        self.phone_numbers.update_phone_number(self.account_id,
                                               self.phone_number,
                                               self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/phone_numbers/' +
                                                       str(self.phone_number),
                                                       self.data)

    def test_update_phone_numbers_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.phone_numbers.update_phone_number(self.account_id,
                                                             self.phone_number,
                                                             self.data)

        assert return_data is self.data

    def test_delete_phone_numbers_request_call(self):
        self.phone_numbers.delete_phone_number(self.account_id,
                                               self.phone_number)
        self.mock_rest_request.delete.assert_called_with(
            'accounts/' + self.account_id + '/phone_numbers/' +
            str(self.phone_number))

    def test_delete_phone_numbers_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.phone_numbers.delete_phone_number(self.account_id,
                                                             self.phone_number)

        assert return_data is self.data
