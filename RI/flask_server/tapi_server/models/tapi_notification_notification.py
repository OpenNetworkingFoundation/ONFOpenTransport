# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_global_class import TapiCommonGlobalClass  # noqa: F401,E501
from tapi_server.models.tapi_common_layer_protocol_name import TapiCommonLayerProtocolName  # noqa: F401,E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: F401,E501
from tapi_server.models.tapi_notification_alarm_info import TapiNotificationAlarmInfo  # noqa: F401,E501
from tapi_server.models.tapi_notification_name_and_value_change import TapiNotificationNameAndValueChange  # noqa: F401,E501
from tapi_server.models.tapi_notification_notification_type import TapiNotificationNotificationType  # noqa: F401,E501
from tapi_server.models.tapi_notification_object_type import TapiNotificationObjectType  # noqa: F401,E501
from tapi_server.models.tapi_notification_source_indicator import TapiNotificationSourceIndicator  # noqa: F401,E501
from tapi_server.models.tapi_notification_tca_info import TapiNotificationTcaInfo  # noqa: F401,E501
from tapi_server import util


class TapiNotificationNotification(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, uuid=None, target_object_type=None, additional_text=None, event_time_stamp=None, additional_info=None, sequence_number=None, tca_info=None, target_object_identifier=None, notification_type=None, target_object_name=None, layer_protocol_name=None, source_indicator=None, alarm_info=None, changed_attributes=None):  # noqa: E501
        """TapiNotificationNotification - a model defined in OpenAPI

        :param name: The name of this TapiNotificationNotification.  # noqa: E501
        :type name: List[TapiCommonNameAndValue]
        :param uuid: The uuid of this TapiNotificationNotification.  # noqa: E501
        :type uuid: str
        :param target_object_type: The target_object_type of this TapiNotificationNotification.  # noqa: E501
        :type target_object_type: TapiNotificationObjectType
        :param additional_text: The additional_text of this TapiNotificationNotification.  # noqa: E501
        :type additional_text: str
        :param event_time_stamp: The event_time_stamp of this TapiNotificationNotification.  # noqa: E501
        :type event_time_stamp: str
        :param additional_info: The additional_info of this TapiNotificationNotification.  # noqa: E501
        :type additional_info: List[TapiCommonNameAndValue]
        :param sequence_number: The sequence_number of this TapiNotificationNotification.  # noqa: E501
        :type sequence_number: int
        :param tca_info: The tca_info of this TapiNotificationNotification.  # noqa: E501
        :type tca_info: TapiNotificationTcaInfo
        :param target_object_identifier: The target_object_identifier of this TapiNotificationNotification.  # noqa: E501
        :type target_object_identifier: str
        :param notification_type: The notification_type of this TapiNotificationNotification.  # noqa: E501
        :type notification_type: TapiNotificationNotificationType
        :param target_object_name: The target_object_name of this TapiNotificationNotification.  # noqa: E501
        :type target_object_name: List[TapiCommonNameAndValue]
        :param layer_protocol_name: The layer_protocol_name of this TapiNotificationNotification.  # noqa: E501
        :type layer_protocol_name: TapiCommonLayerProtocolName
        :param source_indicator: The source_indicator of this TapiNotificationNotification.  # noqa: E501
        :type source_indicator: TapiNotificationSourceIndicator
        :param alarm_info: The alarm_info of this TapiNotificationNotification.  # noqa: E501
        :type alarm_info: TapiNotificationAlarmInfo
        :param changed_attributes: The changed_attributes of this TapiNotificationNotification.  # noqa: E501
        :type changed_attributes: List[TapiNotificationNameAndValueChange]
        """
        self.openapi_types = {
            'name': List[TapiCommonNameAndValue],
            'uuid': str,
            'target_object_type': TapiNotificationObjectType,
            'additional_text': str,
            'event_time_stamp': str,
            'additional_info': List[TapiCommonNameAndValue],
            'sequence_number': int,
            'tca_info': TapiNotificationTcaInfo,
            'target_object_identifier': str,
            'notification_type': TapiNotificationNotificationType,
            'target_object_name': List[TapiCommonNameAndValue],
            'layer_protocol_name': TapiCommonLayerProtocolName,
            'source_indicator': TapiNotificationSourceIndicator,
            'alarm_info': TapiNotificationAlarmInfo,
            'changed_attributes': List[TapiNotificationNameAndValueChange]
        }

        self.attribute_map = {
            'name': 'name',
            'uuid': 'uuid',
            'target_object_type': 'target-object-type',
            'additional_text': 'additional-text',
            'event_time_stamp': 'event-time-stamp',
            'additional_info': 'additional-info',
            'sequence_number': 'sequence-number',
            'tca_info': 'tca-info',
            'target_object_identifier': 'target-object-identifier',
            'notification_type': 'notification-type',
            'target_object_name': 'target-object-name',
            'layer_protocol_name': 'layer-protocol-name',
            'source_indicator': 'source-indicator',
            'alarm_info': 'alarm-info',
            'changed_attributes': 'changed-attributes'
        }

        self._name = name
        self._uuid = uuid
        self._target_object_type = target_object_type
        self._additional_text = additional_text
        self._event_time_stamp = event_time_stamp
        self._additional_info = additional_info
        self._sequence_number = sequence_number
        self._tca_info = tca_info
        self._target_object_identifier = target_object_identifier
        self._notification_type = notification_type
        self._target_object_name = target_object_name
        self._layer_protocol_name = layer_protocol_name
        self._source_indicator = source_indicator
        self._alarm_info = alarm_info
        self._changed_attributes = changed_attributes

    @classmethod
    def from_dict(cls, dikt) -> 'TapiNotificationNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.notification.Notification of this TapiNotificationNotification.  # noqa: E501
        :rtype: TapiNotificationNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this TapiNotificationNotification.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this TapiNotificationNotification.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapiNotificationNotification.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this TapiNotificationNotification.
        :type name: List[TapiCommonNameAndValue]
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this TapiNotificationNotification.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity.                      UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters.                      Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}                       Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The uuid of this TapiNotificationNotification.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this TapiNotificationNotification.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity.                      UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters.                      Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}                       Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param uuid: The uuid of this TapiNotificationNotification.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def target_object_type(self):
        """Gets the target_object_type of this TapiNotificationNotification.


        :return: The target_object_type of this TapiNotificationNotification.
        :rtype: TapiNotificationObjectType
        """
        return self._target_object_type

    @target_object_type.setter
    def target_object_type(self, target_object_type):
        """Sets the target_object_type of this TapiNotificationNotification.


        :param target_object_type: The target_object_type of this TapiNotificationNotification.
        :type target_object_type: TapiNotificationObjectType
        """

        self._target_object_type = target_object_type

    @property
    def additional_text(self):
        """Gets the additional_text of this TapiNotificationNotification.

        none  # noqa: E501

        :return: The additional_text of this TapiNotificationNotification.
        :rtype: str
        """
        return self._additional_text

    @additional_text.setter
    def additional_text(self, additional_text):
        """Sets the additional_text of this TapiNotificationNotification.

        none  # noqa: E501

        :param additional_text: The additional_text of this TapiNotificationNotification.
        :type additional_text: str
        """

        self._additional_text = additional_text

    @property
    def event_time_stamp(self):
        """Gets the event_time_stamp of this TapiNotificationNotification.

        none  # noqa: E501

        :return: The event_time_stamp of this TapiNotificationNotification.
        :rtype: str
        """
        return self._event_time_stamp

    @event_time_stamp.setter
    def event_time_stamp(self, event_time_stamp):
        """Sets the event_time_stamp of this TapiNotificationNotification.

        none  # noqa: E501

        :param event_time_stamp: The event_time_stamp of this TapiNotificationNotification.
        :type event_time_stamp: str
        """

        self._event_time_stamp = event_time_stamp

    @property
    def additional_info(self):
        """Gets the additional_info of this TapiNotificationNotification.

        none  # noqa: E501

        :return: The additional_info of this TapiNotificationNotification.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this TapiNotificationNotification.

        none  # noqa: E501

        :param additional_info: The additional_info of this TapiNotificationNotification.
        :type additional_info: List[TapiCommonNameAndValue]
        """

        self._additional_info = additional_info

    @property
    def sequence_number(self):
        """Gets the sequence_number of this TapiNotificationNotification.

        A monotonous increasing sequence number associated with the notification.                      The exact semantics of how this sequence number is assigned (per channel or subscription or source or system) is left undefined.  # noqa: E501

        :return: The sequence_number of this TapiNotificationNotification.
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this TapiNotificationNotification.

        A monotonous increasing sequence number associated with the notification.                      The exact semantics of how this sequence number is assigned (per channel or subscription or source or system) is left undefined.  # noqa: E501

        :param sequence_number: The sequence_number of this TapiNotificationNotification.
        :type sequence_number: int
        """

        self._sequence_number = sequence_number

    @property
    def tca_info(self):
        """Gets the tca_info of this TapiNotificationNotification.


        :return: The tca_info of this TapiNotificationNotification.
        :rtype: TapiNotificationTcaInfo
        """
        return self._tca_info

    @tca_info.setter
    def tca_info(self, tca_info):
        """Sets the tca_info of this TapiNotificationNotification.


        :param tca_info: The tca_info of this TapiNotificationNotification.
        :type tca_info: TapiNotificationTcaInfo
        """

        self._tca_info = tca_info

    @property
    def target_object_identifier(self):
        """Gets the target_object_identifier of this TapiNotificationNotification.

        none  # noqa: E501

        :return: The target_object_identifier of this TapiNotificationNotification.
        :rtype: str
        """
        return self._target_object_identifier

    @target_object_identifier.setter
    def target_object_identifier(self, target_object_identifier):
        """Sets the target_object_identifier of this TapiNotificationNotification.

        none  # noqa: E501

        :param target_object_identifier: The target_object_identifier of this TapiNotificationNotification.
        :type target_object_identifier: str
        """

        self._target_object_identifier = target_object_identifier

    @property
    def notification_type(self):
        """Gets the notification_type of this TapiNotificationNotification.


        :return: The notification_type of this TapiNotificationNotification.
        :rtype: TapiNotificationNotificationType
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this TapiNotificationNotification.


        :param notification_type: The notification_type of this TapiNotificationNotification.
        :type notification_type: TapiNotificationNotificationType
        """

        self._notification_type = notification_type

    @property
    def target_object_name(self):
        """Gets the target_object_name of this TapiNotificationNotification.

        none  # noqa: E501

        :return: The target_object_name of this TapiNotificationNotification.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._target_object_name

    @target_object_name.setter
    def target_object_name(self, target_object_name):
        """Sets the target_object_name of this TapiNotificationNotification.

        none  # noqa: E501

        :param target_object_name: The target_object_name of this TapiNotificationNotification.
        :type target_object_name: List[TapiCommonNameAndValue]
        """

        self._target_object_name = target_object_name

    @property
    def layer_protocol_name(self):
        """Gets the layer_protocol_name of this TapiNotificationNotification.


        :return: The layer_protocol_name of this TapiNotificationNotification.
        :rtype: TapiCommonLayerProtocolName
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name):
        """Sets the layer_protocol_name of this TapiNotificationNotification.


        :param layer_protocol_name: The layer_protocol_name of this TapiNotificationNotification.
        :type layer_protocol_name: TapiCommonLayerProtocolName
        """

        self._layer_protocol_name = layer_protocol_name

    @property
    def source_indicator(self):
        """Gets the source_indicator of this TapiNotificationNotification.


        :return: The source_indicator of this TapiNotificationNotification.
        :rtype: TapiNotificationSourceIndicator
        """
        return self._source_indicator

    @source_indicator.setter
    def source_indicator(self, source_indicator):
        """Sets the source_indicator of this TapiNotificationNotification.


        :param source_indicator: The source_indicator of this TapiNotificationNotification.
        :type source_indicator: TapiNotificationSourceIndicator
        """

        self._source_indicator = source_indicator

    @property
    def alarm_info(self):
        """Gets the alarm_info of this TapiNotificationNotification.


        :return: The alarm_info of this TapiNotificationNotification.
        :rtype: TapiNotificationAlarmInfo
        """
        return self._alarm_info

    @alarm_info.setter
    def alarm_info(self, alarm_info):
        """Sets the alarm_info of this TapiNotificationNotification.


        :param alarm_info: The alarm_info of this TapiNotificationNotification.
        :type alarm_info: TapiNotificationAlarmInfo
        """

        self._alarm_info = alarm_info

    @property
    def changed_attributes(self):
        """Gets the changed_attributes of this TapiNotificationNotification.

        none  # noqa: E501

        :return: The changed_attributes of this TapiNotificationNotification.
        :rtype: List[TapiNotificationNameAndValueChange]
        """
        return self._changed_attributes

    @changed_attributes.setter
    def changed_attributes(self, changed_attributes):
        """Sets the changed_attributes of this TapiNotificationNotification.

        none  # noqa: E501

        :param changed_attributes: The changed_attributes of this TapiNotificationNotification.
        :type changed_attributes: List[TapiNotificationNameAndValueChange]
        """

        self._changed_attributes = changed_attributes