import pykazoo.faxes
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestFaxes(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.faxes = pykazoo.faxes.Faxes(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_faxes_request_call(self):
        self.faxes.get_faxes(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/faxes/outgoing',
                                                      self.params)

    def test_get_faxes_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.faxes.get_faxes(self.account_id, self.params)

        assert return_data is self.data

    def test_create_fax_request_call(self):
        self.faxes.create_fax(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/faxes/outgoing',
                                                      self.data)

    def test_create_fax_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.faxes.create_fax(self.account_id, self.data)

        assert return_data is self.data
