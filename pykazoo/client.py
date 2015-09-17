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
    """ PyKazooClient is used to access the various API objects. It allows
        state, such as API urls and authentication tokens, to be easily shared
        between the various API objects without the API consumer needing
        to manage them.

        :param api_url: The root URL that the API client should use (example:
                        https://localhost/v2)
        :param rest_request: The request client to use.
            (optional, default: pykazoo.RestRequest())
        :type api_url: str
        :type rest_request: pykazoo.restrequest.RestRequest
    """

    def __init__(self, api_url, rest_request=pykazoo.restrequest):
        self._rest_request = rest_request.RestRequest(api_url)

        self.accounts = Accounts(self._rest_request)
        """ Instance of :class:`pykazoo.accounts.Accounts`"""

        self.agents = Agents(self._rest_request)
        """ Instance of :class:`pykazoo.agents.Agents`"""

        self.authentication = Authentication(self._rest_request)
        """ Instance of :class:`pykazoo.authentication.Authentication`"""

        self.callflows = Callflows(self._rest_request)
        """ Instance of :class:`pykazoo.callflows.Callflows`"""

        self.cdrs = CDRs(self._rest_request)
        """ Instance of :class:`pykazoo.cdrs.CDRs`"""

        self.clicktocalls = ClickToCalls(self._rest_request)
        """ Instance of :class:`pykazoo.clicktocalls.ClickToCalls`"""

        self.conferences = Conferences(self._rest_request)
        """ Instance of :class:`pykazoo.conferences.Conferences`"""

        self.devices = Devices(self._rest_request)
        """ Instance of :class:`pykazoo.devices.Devices`"""

        self.directories = Directories(self._rest_request)
        """ Instance of :class:`pykazoo.directories.Directories`"""

        self.faxes = Faxes(self._rest_request)
        """ Instance of :class:`pykazoo.faxes.Faxes`"""

        self.hotdesks = Hotdesks(self._rest_request)
        """ Instance of :class:`pykazoo.hotdesks.HotDesks`"""

        self.media = Media(self._rest_request)
        """ Instance of :class:`pykazoo.media.Media`"""

        self.menus = Menus(self._rest_request)
        """ Instance of :class:`pykazoo.menus.Menus`"""

        self.metaflows = Metaflows(self._rest_request)
        """ Instance of :class:`pykazoo.metaflows.MetaFlows`"""

        self.phonenumbers = PhoneNumbers(self._rest_request)
        """ Instance of :class:`pykazoo.phonenumbers.PhoneNumbers`"""

        self.queues = Queues(self._rest_request)
        """ Instance of :class:`pykazoo.queues.Queues`"""

        self.quickcalls = QuickCalls(self._rest_request)
        """ Instance of :class:`pykazoo.quickcalls.QuickCalls`"""

        self.resources = Resources(self._rest_request)
        """ Instance of :class:`pykazoo.resources.Resources`"""

        self.timedroutes = TimedRoutes(self._rest_request)
        """ Instance of :class:`pykazoo.timedroutes.TimedRoutes`"""

        self.users = Users(self._rest_request)
        """ Instance of :class:`pykazoo.users.Users`"""

        self.voicemailboxes = VoicemailBoxes(self._rest_request)
        """ Instance of :class:`pykazoo.voicemailboxes.VoiceMailBoxes`"""

        self.webhooks = Webhooks(self._rest_request)
        """ Instance of :class:`pykazoo.webhooks.Webhooks`"""
