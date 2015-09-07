import pykazoo.resources
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec


class TestDevices(TestCase):
    def setUp(self):
        self.mock_rest_request = create_autospec(
            pykazoo.restrequest.RestRequest)

        self.resources = pykazoo.resources.Resources(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.resource_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_resources_request_call(self):
        self.resources.get_resources(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/resources',
                                                      self.params)

    def test_get_resources_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.resources.get_resources(self.account_id,
                                                   self.params)

        assert return_data is self.data

    def test_get_resource_request_call(self):
        self.resources.get_resource(self.account_id, self.resource_id,
                                    self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/resources/' +
                                                      self.resource_id,
                                                      self.params)

    def test_get_resource_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.resources.get_resource(self.account_id,
                                                  self.resource_id,
                                                  self.params)

        assert return_data is self.data

    def test_create_resource_request_call(self):
        self.resources.create_resource(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/resources',
                                                      self.data)

    def test_create_resource_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.resources.create_resource(self.account_id,
                                                     self.data)

        assert return_data is self.data

    def test_update_resource_request_call(self):
        self.resources.update_resource(self.account_id, self.resource_id,
                                       self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/resources/' +
                                                       self.resource_id,
                                                       self.data)

    def test_update_resource_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.resources.update_resource(self.account_id,
                                                     self.resource_id,
                                                     self.data)

        assert return_data is self.data

    def test_delete_resource_request_call(self):
        self.resources.delete_resource(self.account_id, self.resource_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/resources/' +
                                                         self.resource_id)

    def test_delete_resource_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.resources.delete_resource(self.account_id,
                                                     self.resource_id)

        assert return_data is self.data
