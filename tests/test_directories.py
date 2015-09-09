import pykazoo.directories
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestDirectories(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.directories = pykazoo.directories.Directories(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.directory_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_directories_request_call(self):
        self.directories.get_directories(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/directories',
                                                      self.params)

    def test_get_directories_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.directories.get_directories(self.account_id,
                                                       self.params)

        assert return_data is self.data

    def test_get_directory_request_call(self):
        self.directories.get_directory(self.account_id, self.directory_id,
                                       self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/directories/' +
                                                      self.directory_id,
                                                      self.params)

    def test_get_directory_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.directories.get_directory(self.account_id,
                                                     self.directory_id,
                                                     self.params)

        assert return_data is self.data

    def test_create_directory_request_call(self):
        self.directories.create_directory(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/directories',
                                                      self.data)

    def test_create_directory_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.directories.create_directory(self.account_id,
                                                        self.data)

        assert return_data is self.data

    def test_update_directory_request_call(self):
        self.directories.update_directory(self.account_id, self.directory_id,
                                          self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/directories/' +
                                                       self.directory_id,
                                                       self.data)

    def test_update_directory_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.directories.update_directory(self.account_id,
                                                        self.directory_id,
                                                        self.data)

        assert return_data is self.data

    def test_delete_directory_request_call(self):
        self.directories.delete_directory(self.account_id, self.directory_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/directories/' +
                                                         self.directory_id)

    def test_delete_directory_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.directories.delete_directory(self.account_id,
                                                        self.directory_id)

        assert return_data is self.data
