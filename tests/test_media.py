import pykazoo.media
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestDevices(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.media = pykazoo.media.Media(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.media_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_all_media_request_call(self):
        self.media.get_all_media(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/media',
                                                      self.params)

    def test_get_all_media_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.media.get_all_media(self.account_id, self.params)

        assert return_data is self.data

    def test_get_media_request_call(self):
        self.media.get_media(self.account_id, self.media_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/media/' +
                                                      self.media_id,
                                                      self.params)

    def test_get_media_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.media.get_media(self.account_id, self.media_id,
                                           self.params)

        assert return_data is self.data

    def test_create_media_request_call(self):
        self.media.create_media(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/media',
                                                      self.data)

    def test_create_media_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.media.create_media(self.account_id, self.data)

        assert return_data is self.data

    def test_update_media_request_call(self):
        self.media.update_media(self.account_id, self.media_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/media/' +
                                                       self.media_id,
                                                       self.data)

    def test_update_media_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.media.update_media(self.account_id,
                                              self.media_id, self.data)

        assert return_data is self.data

    def test_delete_media_request_call(self):
        self.media.delete_media(self.account_id, self.media_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/media/' +
                                                         self.media_id)

    def test_delete_media_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.media.delete_media(self.account_id, self.media_id)

        assert return_data is self.data

    def test_get_raw_media_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.media.get_raw_media(self.account_id, self.media_id,
                                               self.params)

        assert return_data is self.data

    def test_get_raw_media_request_call(self):
        self.media.get_raw_media(self.account_id, self.media_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/media/' +
                                                      self.media_id + '/raw',
                                                      self.params)

    def test_update_raw_media_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.media.update_raw_media(self.account_id,
                                                  self.media_id, self.data)

        assert return_data is self.data

    def test_update_raw_media_request_call(self):
        self.media.update_raw_media(self.account_id, self.media_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/media/' +
                                                       self.media_id + '/raw',
                                                       self.data,
                                                       'application/x-base64')
