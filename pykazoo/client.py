import pykazoo.restrequest
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


class PyKazooClient:
    def __init__(self, api_url, rest_request=pykazoo.restrequest):
        self._rest_request = rest_request.RestRequest(api_url)
        self.accounts = Accounts(self._rest_request)
        self.agents = Agents(self._rest_request)
        self.authentication = Authentication(self._rest_request)
        self.callflows = Callflows(self._rest_request)
        self.cdrs = CDRs(self._rest_request)
        self.clicktocalls = ClickToCalls(self._rest_request)
        self.conferences = Conferences(self._rest_request)
        self.devices = Devices(self._rest_request)
        self.directories = Directories(self._rest_request)
        self.faxes = Faxes(self._rest_request)
        self.hotdesks = Hotdesks(self._rest_request)
        self.media = Media(self._rest_request)
        self.menus = Menus(self._rest_request)
        self.metaflows = Metaflows(self._rest_request)
        self.phonenumbers = PhoneNumbers(self._rest_request)
        self.queues = Queues(self._rest_request)
        self.quickcalls = QuickCalls(self._rest_request)
        self.resources = Resources(self._rest_request)
        self.timedroutes = TimedRoutes(self._rest_request)
        self.users = Users(self._rest_request)
        self.voicemailboxes = VoicemailBoxes(self._rest_request)
        self.webhooks = Webhooks(self._rest_request)
