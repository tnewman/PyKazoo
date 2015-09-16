import pykazoo.metaflows
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestMetaflows(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.metaflows = pykazoo.metaflows.Metaflows(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.device_id = '123123213rhh798ahfhewa'
        self.callflow_id = '32432432432j8jr98ajr'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_account_metaflows_request_call(self):
        self.metaflows.get_account_metaflows(self.account_id)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/metaflows', None)

    def test_get_account_metaflows_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.metaflows.get_account_metaflows(self.account_id)

        assert return_data is self.data

    def test_get_callflow_metaflows_request_call(self):
        self.metaflows.get_callflow_metaflows(self.account_id,
                                              self.callflow_id)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/callflows/' +
                                                      self.callflow_id +
                                                      '/metaflows', None)

    def test_get_callflow_metaflows_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.metaflows.get_callflow_metaflows(self.account_id,
                                                            self.callflow_id)

        assert return_data is self.data

    def test_get_device_metaflows_request_call(self):
        self.metaflows.get_device_metaflows(self.account_id,
                                            self.device_id)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/devices/' +
                                                      self.device_id +
                                                      '/metaflows', None)

    def test_get_device_metaflows_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.metaflows.get_device_metaflows(self.account_id,
                                                          self.device_id)

        assert return_data is self.data

    def test_update_account_metaflows_request_call(self):
        self.metaflows.update_account_metaflows(self.account_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/metaflows', self.data)

    def test_update_account_metaflows_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.metaflows.update_account_metaflows(self.account_id,
                                                              self.data)

        assert return_data is self.data

    def test_update_callflow_metaflows_request_call(self):
        self.metaflows.update_callflow_metaflows(self.account_id,
                                                 self.callflow_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/callflows/' +
                                                       self.callflow_id +
                                                       '/metaflows', self.data)

    def test_update_callflow_metaflows_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.metaflows.update_callflow_metaflows(
            self.account_id, self.callflow_id, self.data)

        assert return_data is self.data

    def test_update_device_metaflows_request_call(self):
        self.metaflows.update_device_metaflows(self.account_id,
                                               self.device_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/devices/' +
                                                       self.device_id +
                                                       '/metaflows', self.data)

    def test_update_device_metaflows_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.metaflows.update_device_metaflows(self.account_id,
                                                             self.device_id,
                                                             self.data)

        assert return_data is self.data

    def test_delete_account_metaflows_request_call(self):
        self.metaflows.delete_account_metaflows(self.account_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/metaflows')

    def test_delete_account_metaflows_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.metaflows.delete_account_metaflows(self.account_id)

        assert return_data is self.data

    def test_delete_callflow_metaflows_request_call(self):
        self.metaflows.delete_callflow_metaflows(self.account_id,
                                                 self.callflow_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/callflows/' +
                                                         self.callflow_id +
                                                         '/metaflows')

    def test_delete_callflow_metaflows_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.metaflows.delete_callflow_metaflows(
            self.account_id, self.callflow_id)

        assert return_data is self.data

    def test_delete_device_metaflows_request_call(self):
        self.metaflows.delete_device_metaflows(self.account_id, self.device_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/devices/' +
                                                         self.device_id +
                                                         '/metaflows')

    def test_delete_device_metaflows_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.metaflows.delete_device_metaflows(self.account_id,
                                                             self.device_id)

        assert return_data is self.data
