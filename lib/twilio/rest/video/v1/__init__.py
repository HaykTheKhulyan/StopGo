# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.video.v1.composition import CompositionList
from twilio.rest.video.v1.composition_settings import CompositionSettingsList
from twilio.rest.video.v1.recording import RecordingList
from twilio.rest.video.v1.recording_settings import RecordingSettingsList
from twilio.rest.video.v1.room import RoomList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Video

        :returns: V1 version of Video
        :rtype: twilio.rest.video.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._composition_settings = None
        self._recordings = None
        self._recording_settings = None
        self._compositions = None
        self._rooms = None

    @property
    def composition_settings(self):
        """
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsList
        """
        if self._composition_settings is None:
            self._composition_settings = CompositionSettingsList(self)
        return self._composition_settings

    @property
    def recordings(self):
        """
        :rtype: twilio.rest.video.v1.recording.RecordingList
        """
        if self._recordings is None:
            self._recordings = RecordingList(self)
        return self._recordings

    @property
    def recording_settings(self):
        """
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsList
        """
        if self._recording_settings is None:
            self._recording_settings = RecordingSettingsList(self)
        return self._recording_settings

    @property
    def compositions(self):
        """
        :rtype: twilio.rest.video.v1.composition.CompositionList
        """
        if self._compositions is None:
            self._compositions = CompositionList(self)
        return self._compositions

    @property
    def rooms(self):
        """
        :rtype: twilio.rest.video.v1.room.RoomList
        """
        if self._rooms is None:
            self._rooms = RoomList(self)
        return self._rooms

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1>'
