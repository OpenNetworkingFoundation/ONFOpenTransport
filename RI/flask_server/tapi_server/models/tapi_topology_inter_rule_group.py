# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_capacity import TapiCommonCapacity  # noqa: F401,E501
from tapi_server.models.tapi_common_capacity_pac import TapiCommonCapacityPac  # noqa: F401,E501
from tapi_server.models.tapi_common_global_class import TapiCommonGlobalClass  # noqa: F401,E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: F401,E501
from tapi_server.models.tapi_topology_cost_characteristic import TapiTopologyCostCharacteristic  # noqa: F401,E501
from tapi_server.models.tapi_topology_latency_characteristic import TapiTopologyLatencyCharacteristic  # noqa: F401,E501
from tapi_server.models.tapi_topology_node_rule_group_ref import TapiTopologyNodeRuleGroupRef  # noqa: F401,E501
from tapi_server.models.tapi_topology_risk_characteristic import TapiTopologyRiskCharacteristic  # noqa: F401,E501
from tapi_server.models.tapi_topology_risk_parameter_pac import TapiTopologyRiskParameterPac  # noqa: F401,E501
from tapi_server.models.tapi_topology_rule import TapiTopologyRule  # noqa: F401,E501
from tapi_server.models.tapi_topology_transfer_cost_pac import TapiTopologyTransferCostPac  # noqa: F401,E501
from tapi_server.models.tapi_topology_transfer_timing_pac import TapiTopologyTransferTimingPac  # noqa: F401,E501
from tapi_server import util


class TapiTopologyInterRuleGroup(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, available_capacity=None, total_potential_capacity=None, name=None, uuid=None, risk_characteristic=None, cost_characteristic=None, latency_characteristic=None, associated_node_rule_group=None, rule=None):  # noqa: E501
        """TapiTopologyInterRuleGroup - a model defined in OpenAPI

        :param available_capacity: The available_capacity of this TapiTopologyInterRuleGroup.  # noqa: E501
        :type available_capacity: TapiCommonCapacity
        :param total_potential_capacity: The total_potential_capacity of this TapiTopologyInterRuleGroup.  # noqa: E501
        :type total_potential_capacity: TapiCommonCapacity
        :param name: The name of this TapiTopologyInterRuleGroup.  # noqa: E501
        :type name: List[TapiCommonNameAndValue]
        :param uuid: The uuid of this TapiTopologyInterRuleGroup.  # noqa: E501
        :type uuid: str
        :param risk_characteristic: The risk_characteristic of this TapiTopologyInterRuleGroup.  # noqa: E501
        :type risk_characteristic: List[TapiTopologyRiskCharacteristic]
        :param cost_characteristic: The cost_characteristic of this TapiTopologyInterRuleGroup.  # noqa: E501
        :type cost_characteristic: List[TapiTopologyCostCharacteristic]
        :param latency_characteristic: The latency_characteristic of this TapiTopologyInterRuleGroup.  # noqa: E501
        :type latency_characteristic: List[TapiTopologyLatencyCharacteristic]
        :param associated_node_rule_group: The associated_node_rule_group of this TapiTopologyInterRuleGroup.  # noqa: E501
        :type associated_node_rule_group: List[TapiTopologyNodeRuleGroupRef]
        :param rule: The rule of this TapiTopologyInterRuleGroup.  # noqa: E501
        :type rule: List[TapiTopologyRule]
        """
        self.openapi_types = {
            'available_capacity': TapiCommonCapacity,
            'total_potential_capacity': TapiCommonCapacity,
            'name': List[TapiCommonNameAndValue],
            'uuid': str,
            'risk_characteristic': List[TapiTopologyRiskCharacteristic],
            'cost_characteristic': List[TapiTopologyCostCharacteristic],
            'latency_characteristic': List[TapiTopologyLatencyCharacteristic],
            'associated_node_rule_group': List[TapiTopologyNodeRuleGroupRef],
            'rule': List[TapiTopologyRule]
        }

        self.attribute_map = {
            'available_capacity': 'available-capacity',
            'total_potential_capacity': 'total-potential-capacity',
            'name': 'name',
            'uuid': 'uuid',
            'risk_characteristic': 'risk-characteristic',
            'cost_characteristic': 'cost-characteristic',
            'latency_characteristic': 'latency-characteristic',
            'associated_node_rule_group': 'associated-node-rule-group',
            'rule': 'rule'
        }

        self._available_capacity = available_capacity
        self._total_potential_capacity = total_potential_capacity
        self._name = name
        self._uuid = uuid
        self._risk_characteristic = risk_characteristic
        self._cost_characteristic = cost_characteristic
        self._latency_characteristic = latency_characteristic
        self._associated_node_rule_group = associated_node_rule_group
        self._rule = rule

    @classmethod
    def from_dict(cls, dikt) -> 'TapiTopologyInterRuleGroup':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.topology.InterRuleGroup of this TapiTopologyInterRuleGroup.  # noqa: E501
        :rtype: TapiTopologyInterRuleGroup
        """
        return util.deserialize_model(dikt, cls)

    @property
    def available_capacity(self):
        """Gets the available_capacity of this TapiTopologyInterRuleGroup.


        :return: The available_capacity of this TapiTopologyInterRuleGroup.
        :rtype: TapiCommonCapacity
        """
        return self._available_capacity

    @available_capacity.setter
    def available_capacity(self, available_capacity):
        """Sets the available_capacity of this TapiTopologyInterRuleGroup.


        :param available_capacity: The available_capacity of this TapiTopologyInterRuleGroup.
        :type available_capacity: TapiCommonCapacity
        """

        self._available_capacity = available_capacity

    @property
    def total_potential_capacity(self):
        """Gets the total_potential_capacity of this TapiTopologyInterRuleGroup.


        :return: The total_potential_capacity of this TapiTopologyInterRuleGroup.
        :rtype: TapiCommonCapacity
        """
        return self._total_potential_capacity

    @total_potential_capacity.setter
    def total_potential_capacity(self, total_potential_capacity):
        """Sets the total_potential_capacity of this TapiTopologyInterRuleGroup.


        :param total_potential_capacity: The total_potential_capacity of this TapiTopologyInterRuleGroup.
        :type total_potential_capacity: TapiCommonCapacity
        """

        self._total_potential_capacity = total_potential_capacity

    @property
    def name(self):
        """Gets the name of this TapiTopologyInterRuleGroup.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this TapiTopologyInterRuleGroup.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapiTopologyInterRuleGroup.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this TapiTopologyInterRuleGroup.
        :type name: List[TapiCommonNameAndValue]
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this TapiTopologyInterRuleGroup.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity.                      UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters.                      Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}                       Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The uuid of this TapiTopologyInterRuleGroup.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this TapiTopologyInterRuleGroup.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity.                      UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters.                      Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}                       Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param uuid: The uuid of this TapiTopologyInterRuleGroup.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def risk_characteristic(self):
        """Gets the risk_characteristic of this TapiTopologyInterRuleGroup.

        A list of risk characteristics for consideration in an analysis of shared risk. Each element of the list represents a specific risk consideration.  # noqa: E501

        :return: The risk_characteristic of this TapiTopologyInterRuleGroup.
        :rtype: List[TapiTopologyRiskCharacteristic]
        """
        return self._risk_characteristic

    @risk_characteristic.setter
    def risk_characteristic(self, risk_characteristic):
        """Sets the risk_characteristic of this TapiTopologyInterRuleGroup.

        A list of risk characteristics for consideration in an analysis of shared risk. Each element of the list represents a specific risk consideration.  # noqa: E501

        :param risk_characteristic: The risk_characteristic of this TapiTopologyInterRuleGroup.
        :type risk_characteristic: List[TapiTopologyRiskCharacteristic]
        """

        self._risk_characteristic = risk_characteristic

    @property
    def cost_characteristic(self):
        """Gets the cost_characteristic of this TapiTopologyInterRuleGroup.

        The list of costs where each cost relates to some aspect of the TopologicalEntity.  # noqa: E501

        :return: The cost_characteristic of this TapiTopologyInterRuleGroup.
        :rtype: List[TapiTopologyCostCharacteristic]
        """
        return self._cost_characteristic

    @cost_characteristic.setter
    def cost_characteristic(self, cost_characteristic):
        """Sets the cost_characteristic of this TapiTopologyInterRuleGroup.

        The list of costs where each cost relates to some aspect of the TopologicalEntity.  # noqa: E501

        :param cost_characteristic: The cost_characteristic of this TapiTopologyInterRuleGroup.
        :type cost_characteristic: List[TapiTopologyCostCharacteristic]
        """

        self._cost_characteristic = cost_characteristic

    @property
    def latency_characteristic(self):
        """Gets the latency_characteristic of this TapiTopologyInterRuleGroup.

        The effect on the latency of a queuing process. This only has significant effect for packet based systems and has a complex characteristic.  # noqa: E501

        :return: The latency_characteristic of this TapiTopologyInterRuleGroup.
        :rtype: List[TapiTopologyLatencyCharacteristic]
        """
        return self._latency_characteristic

    @latency_characteristic.setter
    def latency_characteristic(self, latency_characteristic):
        """Sets the latency_characteristic of this TapiTopologyInterRuleGroup.

        The effect on the latency of a queuing process. This only has significant effect for packet based systems and has a complex characteristic.  # noqa: E501

        :param latency_characteristic: The latency_characteristic of this TapiTopologyInterRuleGroup.
        :type latency_characteristic: List[TapiTopologyLatencyCharacteristic]
        """

        self._latency_characteristic = latency_characteristic

    @property
    def associated_node_rule_group(self):
        """Gets the associated_node_rule_group of this TapiTopologyInterRuleGroup.

        none  # noqa: E501

        :return: The associated_node_rule_group of this TapiTopologyInterRuleGroup.
        :rtype: List[TapiTopologyNodeRuleGroupRef]
        """
        return self._associated_node_rule_group

    @associated_node_rule_group.setter
    def associated_node_rule_group(self, associated_node_rule_group):
        """Sets the associated_node_rule_group of this TapiTopologyInterRuleGroup.

        none  # noqa: E501

        :param associated_node_rule_group: The associated_node_rule_group of this TapiTopologyInterRuleGroup.
        :type associated_node_rule_group: List[TapiTopologyNodeRuleGroupRef]
        """

        self._associated_node_rule_group = associated_node_rule_group

    @property
    def rule(self):
        """Gets the rule of this TapiTopologyInterRuleGroup.

        none  # noqa: E501

        :return: The rule of this TapiTopologyInterRuleGroup.
        :rtype: List[TapiTopologyRule]
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this TapiTopologyInterRuleGroup.

        none  # noqa: E501

        :param rule: The rule of this TapiTopologyInterRuleGroup.
        :type rule: List[TapiTopologyRule]
        """

        self._rule = rule