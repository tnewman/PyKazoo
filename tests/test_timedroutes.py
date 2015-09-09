import pykazoo.restrequest
import pykazoo.timedroutes
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestDirectories(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.timed_routes = pykazoo.timedroutes.TimedRoutes(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.timed_route_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_timed_routes_request_call(self):
        self.timed_routes.get_timed_routes(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/temporal_rules',
                                                      self.params)

    def test_get_timed_routes_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.timed_routes.get_timed_routes(self.account_id,
                                                         self.params)

        assert return_data is self.data

    def test_get_timed_route_request_call(self):
        self.timed_routes.get_timed_route(self.account_id, self.timed_route_id,
                                          self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/temporal_rules/' +
                                                      self.timed_route_id,
                                                      self.params)

    def test_get_timed_route_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.timed_routes.get_timed_route(self.account_id,
                                                        self.timed_route_id,
                                                        self.params)

        assert return_data is self.data

    def test_create_timed_route_request_call(self):
        self.timed_routes.create_timed_route(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/temporal_rules',
                                                      self.data)

    def test_create_timed_route_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.timed_routes.create_timed_route(self.account_id,
                                                           self.data)

        assert return_data is self.data

    def test_update_timed_route_request_call(self):
        self.timed_routes.update_timed_route(self.account_id,
                                             self.timed_route_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/temporal_rules/' +
                                                       self.timed_route_id,
                                                       self.data)

    def test_update_timed_route_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.timed_routes.update_timed_route(self.account_id,
                                                           self.timed_route_id,
                                                           self.data)

        assert return_data is self.data

    def test_delete_timed_route_request_call(self):
        self.timed_routes.delete_timed_route(self.account_id,
                                             self.timed_route_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/temporal_rules/' +
                                                         self.timed_route_id)

    def test_delete_timed_route_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.timed_routes.delete_timed_route(self.account_id,
                                                           self.timed_route_id)

        assert return_data is self.data
