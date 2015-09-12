import pykazoo.conferences
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestDirectories(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.conferences = pykazoo.conferences.Conferences(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.conference_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_conferences_request_call(self):
        self.conferences.get_conferences(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/conferences',
                                                      self.params)

    def test_get_conferences_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.conferences.get_conferences(self.account_id,
                                                       self.params)

        assert return_data is self.data

    def test_get_conference_request_call(self):
        self.conferences.get_conference(self.account_id, self.conference_id,
                                        self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/conferences/' +
                                                      self.conference_id,
                                                      self.params)

    def test_get_conference_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.conferences.get_conference(self.account_id,
                                                      self.conference_id,
                                                      self.params)

        assert return_data is self.data

    def test_create_conference_request_call(self):
        self.conferences.create_conference(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/conferences',
                                                      self.data)

    def test_create_conference_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.conferences.create_conference(self.account_id,
                                                         self.data)

        assert return_data is self.data

    def test_update_conference_request_call(self):
        self.conferences.update_conference(self.account_id,
                                           self.conference_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/conferences/' +
                                                       self.conference_id,
                                                       self.data)

    def test_update_conference_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.conferences.update_conference(self.account_id,
                                                         self.conference_id,
                                                         self.data)

        assert return_data is self.data

    def test_delete_conference_request_call(self):
        self.conferences.delete_conference(self.account_id, self.conference_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/conferences/' +
                                                         self.conference_id)

    def test_delete_conference_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.conferences.delete_conference(self.account_id,
                                                         self.conference_id)

        assert return_data is self.data
