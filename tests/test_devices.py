import pykazoo.devices
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestDevices(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.devices = pykazoo.devices.Devices(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.device_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_devices_request_call(self):
        self.devices.get_devices(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/devices',
                                                      self.params)

    def test_get_devices_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.devices.get_devices(self.account_id, self.params)

        assert return_data is self.data

    def test_get_device_request_call(self):
        self.devices.get_device(self.account_id, self.device_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/devices/' +
                                                      self.device_id,
                                                      self.params)

    def test_get_device_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.devices.get_device(self.account_id, self.device_id,
                                              self.params)

        assert return_data is self.data

    def test_create_device_request_call(self):
        self.devices.create_device(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/devices',
                                                      self.data)

    def test_create_device_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.devices.create_device(self.account_id, self.data)

        assert return_data is self.data

    def test_update_device_request_call(self):
        self.devices.update_device(self.account_id, self.device_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/devices/' +
                                                       self.device_id,
                                                       self.data)

    def test_update_device_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.devices.update_device(self.account_id,
                                                 self.device_id, self.data)

        assert return_data is self.data

    def test_delete_device_request_call(self):
        self.devices.delete_device(self.account_id, self.device_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/devices/' +
                                                         self.device_id)

    def test_delete_device_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.devices.delete_device(self.account_id,
                                                 self.device_id)

        assert return_data is self.data

    def test_get_devices_status_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.devices.get_devices_status(self.account_id,
                                                      self.params)

        assert return_data is self.data

    def test_get_devices_status_request_call(self):
        self.devices.get_devices_status(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/devices/status',
                                                      self.params)
