class VoicemailBoxes:
    """  2600hz Kazoo VoicemailBoxes API.

        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, rest_request):
        self.rest_request = rest_request

    def get_voicemail_boxes(self, account_id, filters):
        """ Get all VoicemailBoxes for an Account.

        :param account_id: ID of Account to get VoicemailBoxes for.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/vmboxes', filters)

    def get_voicemail_box(self, account_id, voicemail_box_id, filters):
        """ Get a specific VoicemailBoxes for an Account.

        :param account_id: ID of Account to get VoicemailBox for.
        :param voicemail_box_id: ID of the VoicemailBox to get.
        :param filters: Kazoo Filter Parameters (see official API docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type voicemail_box_id: str
        :type filters: dict
        :rtype: dict
        """
        return self.rest_request.get('accounts/' + str(account_id) +
                                     '/vmboxes/' + str(voicemail_box_id),
                                     filters)

    def create_voicemail_box(self, account_id, data):
        """ Create a VoicemailBoxes

        :param account_id: ID of Account to create VoicemailBox for.
        :param data: Kazoo VoicemailBox data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.put('accounts/' + str(account_id) +
                                     '/vmboxes', data)

    def update_voicemail_box(self, account_id, voicemail_box_id, data):
        """ Updates a VoicemailBox

        :param account_id: ID of Account to update VoicemailBox for.
        :param voicemail_box_id: ID of User to update.
        :param data: Kazoo VoicemailBox data (see official API Docs).
        :return: Kazoo Data (see official API docs).
        :type account_id: str
        :type voicemail_box_id: str
        :type data: dict
        :rtype: dict
        """
        return self.rest_request.post('accounts/' + str(account_id) +
                                      '/vmboxes/' + str(voicemail_box_id),
                                      data)

    def delete_voicemail_box(self, account_id, voicemail_box_id):
        """ Deletes a VoicemailBoxes

        :param account_id: ID of Account to delete VoicemailBox from.
        :param voicemail_box_id: ID of VoicemailBox to delete.
        :return: Kazoo Data (see official API docs).
        :rtype: dict
        """
        return self.rest_request.delete('accounts/' + str(account_id) +
                                        '/vmboxes/' + str(voicemail_box_id))
