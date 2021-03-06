# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_administrative_state import TapiCommonAdministrativeState  # noqa: F401,E501
from tapi_server.models.tapi_common_capacity import TapiCommonCapacity  # noqa: F401,E501
from tapi_server.models.tapi_common_layer_protocol_name import TapiCommonLayerProtocolName  # noqa: F401,E501
from tapi_server.models.tapi_common_lifecycle_state import TapiCommonLifecycleState  # noqa: F401,E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: F401,E501
from tapi_server.models.tapi_common_operational_state import TapiCommonOperationalState  # noqa: F401,E501
from tapi_server.models.tapi_common_port_direction import TapiCommonPortDirection  # noqa: F401,E501
from tapi_server.models.tapi_common_port_role import TapiCommonPortRole  # noqa: F401,E501
from tapi_server.models.tapi_common_service_interface_point_ref import TapiCommonServiceInterfacePointRef  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_connection_end_point_ref import TapiConnectivityConnectionEndPointRef  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_connectivity_service_end_point import TapiConnectivityConnectivityServiceEndPoint  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_protection_role import TapiConnectivityProtectionRole  # noqa: F401,E501
from tapi_server.models.tapi_photonic_media_end_point_augmentation1 import TapiPhotonicMediaEndPointAugmentation1  # noqa: F401,E501
from tapi_server.models.tapi_photonic_media_end_point_augmentation2 import TapiPhotonicMediaEndPointAugmentation2  # noqa: F401,E501
from tapi_server.models.tapi_photonic_media_media_channel_service_interface_point_spec import TapiPhotonicMediaMediaChannelServiceInterfacePointSpec  # noqa: F401,E501
from tapi_server.models.tapi_photonic_media_otsi_connectivity_service_end_point_spec import TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec  # noqa: F401,E501
from tapi_server import util


class TapiConnectivityConnectivityserviceEndPoint(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, operational_state=None, lifecycle_state=None, administrative_state=None, name=None, local_id=None, protection_role=None, role=None, service_interface_point=None, layer_protocol_name=None, layer_protocol_qualifier=None, connection_end_point=None, direction=None, capacity=None, media_channel_service_interface_point_spec=None, otsi_connectivity_service_end_point_spec=None):  # noqa: E501
        """TapiConnectivityConnectivityserviceEndPoint - a model defined in OpenAPI

        :param operational_state: The operational_state of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type operational_state: TapiCommonOperationalState
        :param lifecycle_state: The lifecycle_state of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type lifecycle_state: TapiCommonLifecycleState
        :param administrative_state: The administrative_state of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type administrative_state: TapiCommonAdministrativeState
        :param name: The name of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type name: List[TapiCommonNameAndValue]
        :param local_id: The local_id of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type local_id: str
        :param protection_role: The protection_role of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type protection_role: TapiConnectivityProtectionRole
        :param role: The role of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type role: TapiCommonPortRole
        :param service_interface_point: The service_interface_point of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type service_interface_point: TapiCommonServiceInterfacePointRef
        :param layer_protocol_name: The layer_protocol_name of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type layer_protocol_name: TapiCommonLayerProtocolName
        :param layer_protocol_qualifier: The layer_protocol_qualifier of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type layer_protocol_qualifier: str
        :param connection_end_point: The connection_end_point of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type connection_end_point: List[TapiConnectivityConnectionEndPointRef]
        :param direction: The direction of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type direction: TapiCommonPortDirection
        :param capacity: The capacity of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type capacity: TapiCommonCapacity
        :param media_channel_service_interface_point_spec: The media_channel_service_interface_point_spec of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type media_channel_service_interface_point_spec: TapiPhotonicMediaMediaChannelServiceInterfacePointSpec
        :param otsi_connectivity_service_end_point_spec: The otsi_connectivity_service_end_point_spec of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :type otsi_connectivity_service_end_point_spec: TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec
        """
        self.openapi_types = {
            'operational_state': TapiCommonOperationalState,
            'lifecycle_state': TapiCommonLifecycleState,
            'administrative_state': TapiCommonAdministrativeState,
            'name': List[TapiCommonNameAndValue],
            'local_id': str,
            'protection_role': TapiConnectivityProtectionRole,
            'role': TapiCommonPortRole,
            'service_interface_point': TapiCommonServiceInterfacePointRef,
            'layer_protocol_name': TapiCommonLayerProtocolName,
            'layer_protocol_qualifier': str,
            'connection_end_point': List[TapiConnectivityConnectionEndPointRef],
            'direction': TapiCommonPortDirection,
            'capacity': TapiCommonCapacity,
            'media_channel_service_interface_point_spec': TapiPhotonicMediaMediaChannelServiceInterfacePointSpec,
            'otsi_connectivity_service_end_point_spec': TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec
        }

        self.attribute_map = {
            'operational_state': 'operational-state',
            'lifecycle_state': 'lifecycle-state',
            'administrative_state': 'administrative-state',
            'name': 'name',
            'local_id': 'local-id',
            'protection_role': 'protection-role',
            'role': 'role',
            'service_interface_point': 'service-interface-point',
            'layer_protocol_name': 'layer-protocol-name',
            'layer_protocol_qualifier': 'layer-protocol-qualifier',
            'connection_end_point': 'connection-end-point',
            'direction': 'direction',
            'capacity': 'capacity',
            'media_channel_service_interface_point_spec': 'media-channel-service-interface-point-spec',
            'otsi_connectivity_service_end_point_spec': 'otsi-connectivity-service-end-point-spec'
        }

        self._operational_state = operational_state
        self._lifecycle_state = lifecycle_state
        self._administrative_state = administrative_state
        self._name = name
        self._local_id = local_id
        self._protection_role = protection_role
        self._role = role
        self._service_interface_point = service_interface_point
        self._layer_protocol_name = layer_protocol_name
        self._layer_protocol_qualifier = layer_protocol_qualifier
        self._connection_end_point = connection_end_point
        self._direction = direction
        self._capacity = capacity
        self._media_channel_service_interface_point_spec = media_channel_service_interface_point_spec
        self._otsi_connectivity_service_end_point_spec = otsi_connectivity_service_end_point_spec

    @classmethod
    def from_dict(cls, dikt) -> 'TapiConnectivityConnectivityserviceEndPoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.connectivity.connectivityservice.EndPoint of this TapiConnectivityConnectivityserviceEndPoint.  # noqa: E501
        :rtype: TapiConnectivityConnectivityserviceEndPoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def operational_state(self):
        """Gets the operational_state of this TapiConnectivityConnectivityserviceEndPoint.


        :return: The operational_state of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: TapiCommonOperationalState
        """
        return self._operational_state

    @operational_state.setter
    def operational_state(self, operational_state):
        """Sets the operational_state of this TapiConnectivityConnectivityserviceEndPoint.


        :param operational_state: The operational_state of this TapiConnectivityConnectivityserviceEndPoint.
        :type operational_state: TapiCommonOperationalState
        """

        self._operational_state = operational_state

    @property
    def lifecycle_state(self):
        """Gets the lifecycle_state of this TapiConnectivityConnectivityserviceEndPoint.


        :return: The lifecycle_state of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: TapiCommonLifecycleState
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """Sets the lifecycle_state of this TapiConnectivityConnectivityserviceEndPoint.


        :param lifecycle_state: The lifecycle_state of this TapiConnectivityConnectivityserviceEndPoint.
        :type lifecycle_state: TapiCommonLifecycleState
        """

        self._lifecycle_state = lifecycle_state

    @property
    def administrative_state(self):
        """Gets the administrative_state of this TapiConnectivityConnectivityserviceEndPoint.


        :return: The administrative_state of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: TapiCommonAdministrativeState
        """
        return self._administrative_state

    @administrative_state.setter
    def administrative_state(self, administrative_state):
        """Sets the administrative_state of this TapiConnectivityConnectivityserviceEndPoint.


        :param administrative_state: The administrative_state of this TapiConnectivityConnectivityserviceEndPoint.
        :type administrative_state: TapiCommonAdministrativeState
        """

        self._administrative_state = administrative_state

    @property
    def name(self):
        """Gets the name of this TapiConnectivityConnectivityserviceEndPoint.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapiConnectivityConnectivityserviceEndPoint.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this TapiConnectivityConnectivityserviceEndPoint.
        :type name: List[TapiCommonNameAndValue]
        """

        self._name = name

    @property
    def local_id(self):
        """Gets the local_id of this TapiConnectivityConnectivityserviceEndPoint.

        none  # noqa: E501

        :return: The local_id of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this TapiConnectivityConnectivityserviceEndPoint.

        none  # noqa: E501

        :param local_id: The local_id of this TapiConnectivityConnectivityserviceEndPoint.
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def protection_role(self):
        """Gets the protection_role of this TapiConnectivityConnectivityserviceEndPoint.


        :return: The protection_role of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: TapiConnectivityProtectionRole
        """
        return self._protection_role

    @protection_role.setter
    def protection_role(self, protection_role):
        """Sets the protection_role of this TapiConnectivityConnectivityserviceEndPoint.


        :param protection_role: The protection_role of this TapiConnectivityConnectivityserviceEndPoint.
        :type protection_role: TapiConnectivityProtectionRole
        """

        self._protection_role = protection_role

    @property
    def role(self):
        """Gets the role of this TapiConnectivityConnectivityserviceEndPoint.


        :return: The role of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: TapiCommonPortRole
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this TapiConnectivityConnectivityserviceEndPoint.


        :param role: The role of this TapiConnectivityConnectivityserviceEndPoint.
        :type role: TapiCommonPortRole
        """

        self._role = role

    @property
    def service_interface_point(self):
        """Gets the service_interface_point of this TapiConnectivityConnectivityserviceEndPoint.


        :return: The service_interface_point of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: TapiCommonServiceInterfacePointRef
        """
        return self._service_interface_point

    @service_interface_point.setter
    def service_interface_point(self, service_interface_point):
        """Sets the service_interface_point of this TapiConnectivityConnectivityserviceEndPoint.


        :param service_interface_point: The service_interface_point of this TapiConnectivityConnectivityserviceEndPoint.
        :type service_interface_point: TapiCommonServiceInterfacePointRef
        """

        self._service_interface_point = service_interface_point

    @property
    def layer_protocol_name(self):
        """Gets the layer_protocol_name of this TapiConnectivityConnectivityserviceEndPoint.


        :return: The layer_protocol_name of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: TapiCommonLayerProtocolName
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name):
        """Sets the layer_protocol_name of this TapiConnectivityConnectivityserviceEndPoint.


        :param layer_protocol_name: The layer_protocol_name of this TapiConnectivityConnectivityserviceEndPoint.
        :type layer_protocol_name: TapiCommonLayerProtocolName
        """

        self._layer_protocol_name = layer_protocol_name

    @property
    def layer_protocol_qualifier(self):
        """Gets the layer_protocol_qualifier of this TapiConnectivityConnectivityserviceEndPoint.

        none  # noqa: E501

        :return: The layer_protocol_qualifier of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: str
        """
        return self._layer_protocol_qualifier

    @layer_protocol_qualifier.setter
    def layer_protocol_qualifier(self, layer_protocol_qualifier):
        """Sets the layer_protocol_qualifier of this TapiConnectivityConnectivityserviceEndPoint.

        none  # noqa: E501

        :param layer_protocol_qualifier: The layer_protocol_qualifier of this TapiConnectivityConnectivityserviceEndPoint.
        :type layer_protocol_qualifier: str
        """

        self._layer_protocol_qualifier = layer_protocol_qualifier

    @property
    def connection_end_point(self):
        """Gets the connection_end_point of this TapiConnectivityConnectivityserviceEndPoint.

        none  # noqa: E501

        :return: The connection_end_point of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: List[TapiConnectivityConnectionEndPointRef]
        """
        return self._connection_end_point

    @connection_end_point.setter
    def connection_end_point(self, connection_end_point):
        """Sets the connection_end_point of this TapiConnectivityConnectivityserviceEndPoint.

        none  # noqa: E501

        :param connection_end_point: The connection_end_point of this TapiConnectivityConnectivityserviceEndPoint.
        :type connection_end_point: List[TapiConnectivityConnectionEndPointRef]
        """

        self._connection_end_point = connection_end_point

    @property
    def direction(self):
        """Gets the direction of this TapiConnectivityConnectivityserviceEndPoint.


        :return: The direction of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: TapiCommonPortDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this TapiConnectivityConnectivityserviceEndPoint.


        :param direction: The direction of this TapiConnectivityConnectivityserviceEndPoint.
        :type direction: TapiCommonPortDirection
        """

        self._direction = direction

    @property
    def capacity(self):
        """Gets the capacity of this TapiConnectivityConnectivityserviceEndPoint.


        :return: The capacity of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: TapiCommonCapacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this TapiConnectivityConnectivityserviceEndPoint.


        :param capacity: The capacity of this TapiConnectivityConnectivityserviceEndPoint.
        :type capacity: TapiCommonCapacity
        """

        self._capacity = capacity

    @property
    def media_channel_service_interface_point_spec(self):
        """Gets the media_channel_service_interface_point_spec of this TapiConnectivityConnectivityserviceEndPoint.


        :return: The media_channel_service_interface_point_spec of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: TapiPhotonicMediaMediaChannelServiceInterfacePointSpec
        """
        return self._media_channel_service_interface_point_spec

    @media_channel_service_interface_point_spec.setter
    def media_channel_service_interface_point_spec(self, media_channel_service_interface_point_spec):
        """Sets the media_channel_service_interface_point_spec of this TapiConnectivityConnectivityserviceEndPoint.


        :param media_channel_service_interface_point_spec: The media_channel_service_interface_point_spec of this TapiConnectivityConnectivityserviceEndPoint.
        :type media_channel_service_interface_point_spec: TapiPhotonicMediaMediaChannelServiceInterfacePointSpec
        """

        self._media_channel_service_interface_point_spec = media_channel_service_interface_point_spec

    @property
    def otsi_connectivity_service_end_point_spec(self):
        """Gets the otsi_connectivity_service_end_point_spec of this TapiConnectivityConnectivityserviceEndPoint.


        :return: The otsi_connectivity_service_end_point_spec of this TapiConnectivityConnectivityserviceEndPoint.
        :rtype: TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec
        """
        return self._otsi_connectivity_service_end_point_spec

    @otsi_connectivity_service_end_point_spec.setter
    def otsi_connectivity_service_end_point_spec(self, otsi_connectivity_service_end_point_spec):
        """Sets the otsi_connectivity_service_end_point_spec of this TapiConnectivityConnectivityserviceEndPoint.


        :param otsi_connectivity_service_end_point_spec: The otsi_connectivity_service_end_point_spec of this TapiConnectivityConnectivityserviceEndPoint.
        :type otsi_connectivity_service_end_point_spec: TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec
        """

        self._otsi_connectivity_service_end_point_spec = otsi_connectivity_service_end_point_spec
