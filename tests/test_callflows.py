import pykazoo.callflows
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec


class TestDevices(TestCase):
    def setUp(self):
        self.mock_rest_request = create_autospec(
            pykazoo.restrequest.RestRequest)

        self.callflows = pykazoo.callflows.Callflows(self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.callflow_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_callflows_request_call(self):
        self.callflows.get_callflows(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/callflows',
                                                      self.params)

    def test_get_callflows_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.callflows.get_callflows(self.account_id,
                                                   self.params)

        assert return_data is self.data

    def test_get_callflow_request_call(self):
        self.callflows.get_callflow(self.account_id, self.callflow_id,
                                    self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/callflows/' +
                                                      self.callflow_id,
                                                      self.params)

    def test_get_callflow_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.callflows.get_callflow(self.account_id,
                                                  self.callflow_id,
                                                  self.params)

        assert return_data is self.data

    def test_create_callflow_request_call(self):
        self.callflows.create_callflow(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/callflows',
                                                      self.data)

    def test_create_callflow_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.callflows.create_callflow(self.account_id,
                                                     self.data)

        assert return_data is self.data

    def test_update_callflow_request_call(self):
        self.callflows.update_callflow(self.account_id, self.callflow_id,
                                       self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/callflows/' +
                                                       self.callflow_id,
                                                       self.data)

    def test_update_callflow_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.callflows.update_callflow(self.account_id,
                                                     self.callflow_id,
                                                     self.data)

        assert return_data is self.data

    def test_delete_callflow_request_call(self):
        self.callflows.delete_callflow(self.account_id, self.callflow_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/callflows/' +
                                                         self.callflow_id)

    def test_delete_callflow_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.callflows.delete_callflow(self.account_id,
                                                     self.callflow_id)

        assert return_data is self.data
