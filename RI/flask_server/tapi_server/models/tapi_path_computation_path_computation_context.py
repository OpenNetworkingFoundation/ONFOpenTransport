# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_path_computation_path import TapiPathComputationPath  # noqa: F401,E501
from tapi_server.models.tapi_path_computation_path_computation_service import TapiPathComputationPathComputationService  # noqa: F401,E501
from tapi_server import util


class TapiPathComputationPathComputationContext(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, path_comp_service=None, path=None):  # noqa: E501
        """TapiPathComputationPathComputationContext - a model defined in OpenAPI

        :param path_comp_service: The path_comp_service of this TapiPathComputationPathComputationContext.  # noqa: E501
        :type path_comp_service: List[TapiPathComputationPathComputationService]
        :param path: The path of this TapiPathComputationPathComputationContext.  # noqa: E501
        :type path: List[TapiPathComputationPath]
        """
        self.openapi_types = {
            'path_comp_service': List[TapiPathComputationPathComputationService],
            'path': List[TapiPathComputationPath]
        }

        self.attribute_map = {
            'path_comp_service': 'path-comp-service',
            'path': 'path'
        }

        self._path_comp_service = path_comp_service
        self._path = path

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPathComputationPathComputationContext':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.path.computation.PathComputationContext of this TapiPathComputationPathComputationContext.  # noqa: E501
        :rtype: TapiPathComputationPathComputationContext
        """
        return util.deserialize_model(dikt, cls)

    @property
    def path_comp_service(self):
        """Gets the path_comp_service of this TapiPathComputationPathComputationContext.

        none  # noqa: E501

        :return: The path_comp_service of this TapiPathComputationPathComputationContext.
        :rtype: List[TapiPathComputationPathComputationService]
        """
        return self._path_comp_service

    @path_comp_service.setter
    def path_comp_service(self, path_comp_service):
        """Sets the path_comp_service of this TapiPathComputationPathComputationContext.

        none  # noqa: E501

        :param path_comp_service: The path_comp_service of this TapiPathComputationPathComputationContext.
        :type path_comp_service: List[TapiPathComputationPathComputationService]
        """

        self._path_comp_service = path_comp_service

    @property
    def path(self):
        """Gets the path of this TapiPathComputationPathComputationContext.

        none  # noqa: E501

        :return: The path of this TapiPathComputationPathComputationContext.
        :rtype: List[TapiPathComputationPath]
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TapiPathComputationPathComputationContext.

        none  # noqa: E501

        :param path: The path of this TapiPathComputationPathComputationContext.
        :type path: List[TapiPathComputationPath]
        """

        self._path = path