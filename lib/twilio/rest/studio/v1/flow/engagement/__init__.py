# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.studio.v1.flow.engagement.engagement_context import EngagementContextList
from twilio.rest.studio.v1.flow.engagement.step import StepList


class EngagementList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, flow_sid):
        """
        Initialize the EngagementList

        :param Version version: Version that contains the resource
        :param flow_sid: Flow Sid.

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementList
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementList
        """
        super(EngagementList, self).__init__(version)

        # Path Solution
        self._solution = {'flow_sid': flow_sid, }
        self._uri = '/Flows/{flow_sid}/Engagements'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams EngagementInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v1.flow.engagement.EngagementInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists EngagementInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v1.flow.engagement.EngagementInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of EngagementInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return EngagementPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EngagementInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return EngagementPage(self._version, response, self._solution)

    def create(self, to, from_, parameters=values.unset):
        """
        Create a new EngagementInstance

        :param unicode to: The Contact phone number to start a Studio Flow Engagement.
        :param unicode from_: The Twilio phone number to send messages or initiate calls from during the Flow Engagement.
        :param dict parameters: JSON data that will be added to your flow's context and can accessed as variables inside your flow.

        :returns: Newly created EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        """
        data = values.of({'To': to, 'From': from_, 'Parameters': serialize.object(parameters), })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return EngagementInstance(self._version, payload, flow_sid=self._solution['flow_sid'], )

    def get(self, sid):
        """
        Constructs a EngagementContext

        :param sid: Engagement Sid.

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementContext
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementContext
        """
        return EngagementContext(self._version, flow_sid=self._solution['flow_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a EngagementContext

        :param sid: Engagement Sid.

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementContext
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementContext
        """
        return EngagementContext(self._version, flow_sid=self._solution['flow_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.EngagementList>'


class EngagementPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the EngagementPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param flow_sid: Flow Sid.

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementPage
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementPage
        """
        super(EngagementPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of EngagementInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        """
        return EngagementInstance(self._version, payload, flow_sid=self._solution['flow_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.EngagementPage>'


class EngagementContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, flow_sid, sid):
        """
        Initialize the EngagementContext

        :param Version version: Version that contains the resource
        :param flow_sid: Flow Sid.
        :param sid: Engagement Sid.

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementContext
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementContext
        """
        super(EngagementContext, self).__init__(version)

        # Path Solution
        self._solution = {'flow_sid': flow_sid, 'sid': sid, }
        self._uri = '/Flows/{flow_sid}/Engagements/{sid}'.format(**self._solution)

        # Dependents
        self._steps = None
        self._engagement_context = None

    def fetch(self):
        """
        Fetch a EngagementInstance

        :returns: Fetched EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return EngagementInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the EngagementInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def steps(self):
        """
        Access the steps

        :returns: twilio.rest.studio.v1.flow.engagement.step.StepList
        :rtype: twilio.rest.studio.v1.flow.engagement.step.StepList
        """
        if self._steps is None:
            self._steps = StepList(
                self._version,
                flow_sid=self._solution['flow_sid'],
                engagement_sid=self._solution['sid'],
            )
        return self._steps

    @property
    def engagement_context(self):
        """
        Access the engagement_context

        :returns: twilio.rest.studio.v1.flow.engagement.engagement_context.EngagementContextList
        :rtype: twilio.rest.studio.v1.flow.engagement.engagement_context.EngagementContextList
        """
        if self._engagement_context is None:
            self._engagement_context = EngagementContextList(
                self._version,
                flow_sid=self._solution['flow_sid'],
                engagement_sid=self._solution['sid'],
            )
        return self._engagement_context

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.EngagementContext {}>'.format(context)


class EngagementInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class Status(object):
        ACTIVE = "active"
        ENDED = "ended"

    def __init__(self, version, payload, flow_sid, sid=None):
        """
        Initialize the EngagementInstance

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        """
        super(EngagementInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'flow_sid': payload['flow_sid'],
            'contact_sid': payload['contact_sid'],
            'contact_channel_address': payload['contact_channel_address'],
            'context': payload['context'],
            'status': payload['status'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {'flow_sid': flow_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: EngagementContext for this EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementContext
        """
        if self._context is None:
            self._context = EngagementContext(
                self._version,
                flow_sid=self._solution['flow_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Engagement.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def flow_sid(self):
        """
        :returns: Flow Sid.
        :rtype: unicode
        """
        return self._properties['flow_sid']

    @property
    def contact_sid(self):
        """
        :returns: Contact Sid.
        :rtype: unicode
        """
        return self._properties['contact_sid']

    @property
    def contact_channel_address(self):
        """
        :returns: The phone number, SIP address or Client identifier that triggered this Engagement.
        :rtype: unicode
        """
        return self._properties['contact_channel_address']

    @property
    def context(self):
        """
        :returns: Flow state.
        :rtype: dict
        """
        return self._properties['context']

    @property
    def status(self):
        """
        :returns: The Status of this Engagement
        :rtype: EngagementInstance.Status
        """
        return self._properties['status']

    @property
    def date_created(self):
        """
        :returns: The date this Engagement was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Engagement was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: Nested resource URLs.
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a EngagementInstance

        :returns: Fetched EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the EngagementInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def steps(self):
        """
        Access the steps

        :returns: twilio.rest.studio.v1.flow.engagement.step.StepList
        :rtype: twilio.rest.studio.v1.flow.engagement.step.StepList
        """
        return self._proxy.steps

    @property
    def engagement_context(self):
        """
        Access the engagement_context

        :returns: twilio.rest.studio.v1.flow.engagement.engagement_context.EngagementContextList
        :rtype: twilio.rest.studio.v1.flow.engagement.engagement_context.EngagementContextList
        """
        return self._proxy.engagement_context

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.EngagementInstance {}>'.format(context)
