import pykazoo.agents
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec


class TestAgents(TestCase):
    def setUp(self):
        self.mock_rest_request = create_autospec(
            pykazoo.restrequest.RestRequest)

        self.agents = pykazoo.agents.Agents(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.agent_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_agents_request_call(self):
        self.agents.get_agents(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/agents',
                                                      self.params)

    def test_get_agents_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.agents.get_agents(self.account_id, self.params)

        assert return_data is self.data

    def test_get_agent_request_call(self):
        self.agents.get_agent(self.account_id, self.agent_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/agents/' +
                                                      self.agent_id,
                                                      self.params)

    def test_get_agent_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.agents.get_agent(self.account_id, self.agent_id,
                                            self.params)

        assert return_data is self.data

    def test_get_agents_stats_request_call(self):
        self.agents.get_agents_stats(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/agents/stats',
                                                      self.params)

    def test_get_agents_stats_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.agents.get_agents_stats(self.account_id,
                                                   self.params)

        assert return_data is self.data
