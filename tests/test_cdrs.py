import pykazoo.cdrs
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestCDRs(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.cdrs = pykazoo.cdrs.CDRs(self.mock_rest_request)
        self.params = {'test': 'params'}
        self.data = {'test': 'data'}

    def test_get_cdrs_request_call(self):
        self.cdrs.get_cdrs(self.params)
        self.mock_rest_request.get.assert_called_with('cdrs', self.params)

    def test_get_cdrs_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.cdrs.get_cdrs(self.params)

        assert return_data is self.data
