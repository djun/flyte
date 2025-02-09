# coding: utf-8

"""
    flyteidl/service/admin.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flyteadmin.models.core_artifact_binding_data import CoreArtifactBindingData  # noqa: F401,E501
from flyteadmin.models.core_artifact_id import CoreArtifactID  # noqa: F401,E501
from flyteadmin.models.core_artifact_tag import CoreArtifactTag  # noqa: F401,E501


class CoreArtifactQuery(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'artifact_id': 'CoreArtifactID',
        'artifact_tag': 'CoreArtifactTag',
        'uri': 'str',
        'binding': 'CoreArtifactBindingData'
    }

    attribute_map = {
        'artifact_id': 'artifact_id',
        'artifact_tag': 'artifact_tag',
        'uri': 'uri',
        'binding': 'binding'
    }

    def __init__(self, artifact_id=None, artifact_tag=None, uri=None, binding=None):  # noqa: E501
        """CoreArtifactQuery - a model defined in Swagger"""  # noqa: E501

        self._artifact_id = None
        self._artifact_tag = None
        self._uri = None
        self._binding = None
        self.discriminator = None

        if artifact_id is not None:
            self.artifact_id = artifact_id
        if artifact_tag is not None:
            self.artifact_tag = artifact_tag
        if uri is not None:
            self.uri = uri
        if binding is not None:
            self.binding = binding

    @property
    def artifact_id(self):
        """Gets the artifact_id of this CoreArtifactQuery.  # noqa: E501


        :return: The artifact_id of this CoreArtifactQuery.  # noqa: E501
        :rtype: CoreArtifactID
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """Sets the artifact_id of this CoreArtifactQuery.


        :param artifact_id: The artifact_id of this CoreArtifactQuery.  # noqa: E501
        :type: CoreArtifactID
        """

        self._artifact_id = artifact_id

    @property
    def artifact_tag(self):
        """Gets the artifact_tag of this CoreArtifactQuery.  # noqa: E501


        :return: The artifact_tag of this CoreArtifactQuery.  # noqa: E501
        :rtype: CoreArtifactTag
        """
        return self._artifact_tag

    @artifact_tag.setter
    def artifact_tag(self, artifact_tag):
        """Sets the artifact_tag of this CoreArtifactQuery.


        :param artifact_tag: The artifact_tag of this CoreArtifactQuery.  # noqa: E501
        :type: CoreArtifactTag
        """

        self._artifact_tag = artifact_tag

    @property
    def uri(self):
        """Gets the uri of this CoreArtifactQuery.  # noqa: E501


        :return: The uri of this CoreArtifactQuery.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this CoreArtifactQuery.


        :param uri: The uri of this CoreArtifactQuery.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def binding(self):
        """Gets the binding of this CoreArtifactQuery.  # noqa: E501

        This is used in the trigger case, where a user specifies a value for an input that is one of the triggering artifacts, or a partition value derived from a triggering artifact.  # noqa: E501

        :return: The binding of this CoreArtifactQuery.  # noqa: E501
        :rtype: CoreArtifactBindingData
        """
        return self._binding

    @binding.setter
    def binding(self, binding):
        """Sets the binding of this CoreArtifactQuery.

        This is used in the trigger case, where a user specifies a value for an input that is one of the triggering artifacts, or a partition value derived from a triggering artifact.  # noqa: E501

        :param binding: The binding of this CoreArtifactQuery.  # noqa: E501
        :type: CoreArtifactBindingData
        """

        self._binding = binding

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CoreArtifactQuery, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CoreArtifactQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
