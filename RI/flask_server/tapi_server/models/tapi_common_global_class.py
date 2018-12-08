# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: F401,E501
from tapi_server import util


class TapiCommonGlobalClass(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, uuid=None):  # noqa: E501
        """TapiCommonGlobalClass - a model defined in OpenAPI

        :param name: The name of this TapiCommonGlobalClass.  # noqa: E501
        :type name: List[TapiCommonNameAndValue]
        :param uuid: The uuid of this TapiCommonGlobalClass.  # noqa: E501
        :type uuid: str
        """
        self.openapi_types = {
            'name': List[TapiCommonNameAndValue],
            'uuid': str
        }

        self.attribute_map = {
            'name': 'name',
            'uuid': 'uuid'
        }

        self._name = name
        self._uuid = uuid

    @classmethod
    def from_dict(cls, dikt) -> 'TapiCommonGlobalClass':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.common.GlobalClass of this TapiCommonGlobalClass.  # noqa: E501
        :rtype: TapiCommonGlobalClass
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this TapiCommonGlobalClass.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this TapiCommonGlobalClass.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapiCommonGlobalClass.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this TapiCommonGlobalClass.
        :type name: List[TapiCommonNameAndValue]
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this TapiCommonGlobalClass.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity.                      UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters.                      Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}                       Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The uuid of this TapiCommonGlobalClass.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this TapiCommonGlobalClass.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity.                      UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters.                      Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}                       Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param uuid: The uuid of this TapiCommonGlobalClass.
        :type uuid: str
        """

        self._uuid = uuid