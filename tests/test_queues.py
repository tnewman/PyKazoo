import pykazoo.queues
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec


class TestQueues(TestCase):
    def setUp(self):
        self.mock_rest_request = create_autospec(
            pykazoo.restrequest.RestRequest)

        self.queues = pykazoo.queues.Queues(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.queue_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_queues_request_call(self):
        self.queues.get_queues(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/queues',
                                                      self.params)

    def test_get_queues_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.queues.get_queues(self.account_id, self.params)

        assert return_data is self.data

    def test_get_queue_request_call(self):
        self.queues.get_queue(self.account_id, self.queue_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/queues/' +
                                                      self.queue_id,
                                                      self.params)

    def test_get_queue_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.queues.get_queue(self.account_id, self.queue_id,
                                            self.params)

        assert return_data is self.data

    def test_create_queue_request_call(self):
        self.queues.create_queue(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/queues',
                                                      self.data)

    def test_create_queue_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.queues.create_queue(self.account_id, self.data)

        assert return_data is self.data

    def test_update_queue_request_call(self):
        self.queues.update_queue(self.account_id, self.queue_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/queues/' +
                                                       self.queue_id,
                                                       self.data)

    def test_update_queue_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.queues.update_queue(self.account_id,
                                               self.queue_id, self.data)

        assert return_data is self.data

    def test_delete_queue_request_call(self):
        self.queues.delete_queue(self.account_id, self.queue_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/queues/' +
                                                         self.queue_id)

    def test_delete_queue_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.queues.delete_queue(self.account_id, self.queue_id)

        assert return_data is self.data

    def test_get_queues_stats_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.queues.get_queues_stats(self.account_id,
                                                   self.params)

        assert return_data is self.data

    def test_get_queues_stats_request_call(self):
        self.queues.get_queues_stats(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/queues/stats',
                                                      self.params)
