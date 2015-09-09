import pykazoo.restrequest
import pykazoo.voicemailboxes
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestVoicemailBoxes(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.voicemail_boxes = pykazoo.voicemailboxes.VoicemailBoxes(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.voicemail_box_id = '234gadf13rhh798ahf54hew4'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_voicemail_boxes_request_call(self):
        self.voicemail_boxes.get_voicemail_boxes(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/vmboxes',
                                                      self.params)

    def test_get_voicemail_boxes_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.voicemail_boxes.get_voicemail_boxes(self.account_id,
                                                               self.params)
        assert return_data is self.data

    def test_get_voicemail_box_request_call(self):
        self.voicemail_boxes.get_voicemail_box(self.account_id,
                                               self.voicemail_box_id,
                                               self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/vmboxes/' +
                                                      self.voicemail_box_id,
                                                      self.params)

    def test_get_voicemail_box_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.voicemail_boxes.get_voicemail_box(
            self.account_id, self.voicemail_box_id, self.params)

        assert return_data is self.data

    def test_create_voicemail_box_request_call(self):
        self.voicemail_boxes.create_voicemail_box(self.account_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/vmboxes',
                                                      self.data)

    def test_create_voicemail_box_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.voicemail_boxes.create_voicemail_box(
            self.account_id, self.data)

        assert return_data is self.data

    def test_update_voicemail_box_request_call(self):
        self.voicemail_boxes.update_voicemail_box(self.account_id,
                                                  self.voicemail_box_id,
                                                  self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/vmboxes/' +
                                                       self.voicemail_box_id,
                                                       self.data)

    def test_update_voicemail_box_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.voicemail_boxes.update_voicemail_box(
            self.account_id, self.voicemail_box_id, self.data)

        assert return_data is self.data

    def test_delete_voicemail_box_request_call(self):
        self.voicemail_boxes.delete_voicemail_box(self.account_id,
                                                  self.voicemail_box_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/vmboxes/' +
                                                         self.voicemail_box_id)

    def test_delete_voicemail_box_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.voicemail_boxes.delete_voicemail_box(
            self.account_id, self.voicemail_box_id)

        assert return_data is self.data
