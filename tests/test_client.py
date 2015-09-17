import pykazoo.client
from unittest import TestCase
from pykazoo.accounts import Accounts
from pykazoo.agents import Agents
from pykazoo.authentication import Authentication
from pykazoo.callflows import Callflows
from pykazoo.cdrs import CDRs
from pykazoo.clicktocalls import ClickToCalls
from pykazoo.conferences import Conferences
from pykazoo.devices import Devices
from pykazoo.directories import Directories
from pykazoo.faxes import Faxes
from pykazoo.hotdesks import Hotdesks
from pykazoo.media import Media
from pykazoo.menus import Menus
from pykazoo.metaflows import Metaflows
from pykazoo.phonenumbers import PhoneNumbers
from pykazoo.queues import Queues
from pykazoo.quickcalls import QuickCalls
from pykazoo.resources import Resources
from pykazoo.timedroutes import TimedRoutes
from pykazoo.users import Users
from pykazoo.voicemailboxes import VoicemailBoxes
from pykazoo.webhooks import Webhooks


class TestDevices(TestCase):
    def setUp(self):
        self.client = pykazoo.client.PyKazooClient('https://localhost:8080/v2')

    def test_map_attributes_to_client_objects(self):
        assert type(self.client.accounts) is Accounts
        assert type(self.client.agents) is Agents
        assert type(self.client.authentication) is Authentication
        assert type(self.client.callflows) is Callflows
        assert type(self.client.cdrs) is CDRs
        assert type(self.client.clicktocalls) is ClickToCalls
        assert type(self.client.conferences) is Conferences
        assert type(self.client.devices) is Devices
        assert type(self.client.directories) is Directories
        assert type(self.client.faxes) is Faxes
        assert type(self.client.hotdesks) is Hotdesks
        assert type(self.client.media) is Media
        assert type(self.client.menus) is Menus
        assert type(self.client.metaflows) is Metaflows
        assert type(self.client.phonenumbers) is PhoneNumbers
        assert type(self.client.queues) is Queues
        assert type(self.client.quickcalls) is QuickCalls
        assert type(self.client.resources) is Resources
        assert type(self.client.timedroutes) is TimedRoutes
        assert type(self.client.users) is Users
        assert type(self.client.voicemailboxes) is VoicemailBoxes
        assert type(self.client.webhooks) is Webhooks
