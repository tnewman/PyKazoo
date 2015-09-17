PyKazoo Quickstart
==================

.. _`2600hz Kazoo Crossbar`: https://2600hz.atlassian.net/wiki/display/APIs/Developer+APIs

Overview
--------
PyKazoo is divided into a series of classes, where each class represents an
API Object provided by `2600hz Kazoo Crossbar`_. Note that only the API
objects and actions described on the wiki are in scope for PyKazoo.

PyKazoo is primarily used through :class:`pykazoo.client.PyKazooClient`, which
provides a convenient wrapper to access all of the API objects.
:class:`pykazoo.client.PyKazooClient` also allows states, such as API urls and
authentication tokens, to be passed into the API objects without manual
intervention by the API consumer. API objects are created when
:class:`pykazoo.client.PyKazooClient`. is created and are provided to the API
consumer as attributes.

Using PyKazoo Client
====================
To use :class:`pykazoo.client.PyKazooClient`, import :mod:`pykazoo.client`
and create an instance of :class:`pykazoo.client.PyKazooClient` with the root
`2600hz Kazoo Crossbar`_ API URL passed into the constructor.

.. code-block:: python

    >>> import pykazoo.client
    >>> client = pykazoo.client.PyKazooClient('https://sampleapiurl:4334/v2')

Authentication
--------------
Most `2600hz Kazoo Crossbar`_ API calls require an authentication token.
:attr:`pykazoo.client.PyKazooClient.authentication` provides
:attr:`~pykazoo.authentication.Authentication.api_auth` for authenticating
using an API token and :attr:`~pykazoo.authentication.Authentication.user_auth`
for authenticating using a username, password and account name.

Once an authentication method succeeds, the authentication token is automatically
cached for use by API objects accessed through
:class:`pykazoo.client.PyKazooClient`. The return data may be useful for later
API calls, such as the account ID, and is converted to a dict for convenience.

.. code-block:: python

    >>> import pykazoo.client
    >>> client = pykazoo.client.PyKazooClient('https://sampleapiurl:4334/v2')
    >>> client.authentication.user_auth('admin', 'admin', 'admin')
    {'request_id': '8e0065981b9f42827576fa37f7637fc6', 'data': {'reseller_id': '06560d759eeb7f095003b681cbb9e1ee', 'owner_id': '59ccb583257cc7a76cf70e6a549e539a', 'account_id': '06560d759eeb7f095003b681cbb9e1ee', 'account_name': 'admin', 'apps': [], 'is_reseller': True, 'language': 'en-us'}, 'auth_token': '56ada10c0f6ffee7c82c0579a9d4f4fc', 'status': 'success', 'page_size': 1, 'revision': 'automatic'}

API Calls
---------
All of the API Objects provided by `2600hz Kazoo Crossbar`_ are available
through :class:`pykazoo.client.PyKazooClient`. Each API Object is documented
in detail; however, data passed to API Objects is described by
`2600hz Kazoo Crossbar`_ and is not duplicated here.

Once an authentication method succeeds, it is often useful to store the account
id for use with other API calls.

.. code-block:: python

    >>> import pykazoo.client
    >>> client = pykazoo.client.PyKazooClient('https://sampleapiurl:4334/v2')
    >>> client.authentication.user_auth('admin', 'admin', 'admin')
    >>> account_id = client.authentication.user_auth('admin', 'admin', 'admin')['data']['account_id']
    >>> client.devices.get_devices(account_id)
    {'request_id': '583891e3902f3a20bc20f777f9dbd0d6', 'data': [{'name': 'test', 'enabled': True, 'id': 'be29cd8e5f2a4b8117ee4729e5548cc4', 'mac_address': '', 'device_type': 'sip_device'}, {'owner_id': '59ccb583257cc7a76cf70e6a549e539a', 'name': "Account Admin's Browserphone", 'enabled': True, 'id': 'a0a87b1847c9c1c7aa9f6b5901f33878', 'mac_address': '', 'device_type': 'sip_device'}], 'auth_token': 'cba16bf5d8cd741091658f691e7dc92b', 'status': 'success', 'page_size': 2, 'revision': '3a60d6b1d452553ed11a483172a68ee4'}

That's It!
----------
That's really all it takes to configure and use PyKazoo. If you are confused,
make sure to review the `2600hz Kazoo Crossbar`_ documentation as it describes
the data and query parameters it expects.