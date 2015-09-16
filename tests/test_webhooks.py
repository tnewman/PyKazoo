import pykazoo.restrequest
import pykazoo.webhooks
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestDevices(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.webhooks = pykazoo.webhooks.Webhooks(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.webhook_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_system_webhooks_request_call(self):
        self.webhooks.get_system_webhooks(self.params)
        self.mock_rest_request.get.assert_called_with('webhooks',
                                                      self.params)

    def test_get_system_webhooks_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.webhooks.get_system_webhooks(self.params)

        assert return_data is self.data

    def test_get_webhooks_request_call(self):
        self.webhooks.get_webhooks(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/webhooks',
                                                      self.params)

    def test_get_webhooks_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.webhooks.get_webhooks(self.account_id, self.params)

        assert return_data is self.data

    def test_get_webhook_request_call(self):
        self.webhooks.get_webhook(self.account_id, self.webhook_id,
                                  self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/webhooks/' +
                                                      self.webhook_id,
                                                      self.params)

    def test_get_webhook_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.webhooks.get_webhook(self.account_id,
                                                self.webhook_id,
                                                self.params)

        assert return_data is self.data

    def test_create_webhook_request_call(self):
        self.webhooks.create_webhook(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/webhooks',
                                                      self.data)

    def test_create_webhook_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.webhooks.create_webhook(self.account_id, self.data)

        assert return_data is self.data

    def test_update_webhook_request_call(self):
        self.webhooks.update_webhook(self.account_id, self.webhook_id,
                                     self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/webhooks/' +
                                                       self.webhook_id,
                                                       self.data)

    def test_update_webhook_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.webhooks.update_webhook(self.account_id,
                                                   self.webhook_id, self.data)

        assert return_data is self.data

    def test_delete_webhook_request_call(self):
        self.webhooks.delete_webhook(self.account_id, self.webhook_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/webhooks/' +
                                                         self.webhook_id)

    def test_delete_webhook_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.webhooks.delete_webhook(self.account_id,
                                                   self.webhook_id)

        assert return_data is self.data
