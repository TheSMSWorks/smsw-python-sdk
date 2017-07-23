# coding: utf-8

"""
    The SMS Works API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ApiKeyResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'key': 'str',
        'secret': 'str'
    }

    attribute_map = {
        'key': 'key',
        'secret': 'secret'
    }

    def __init__(self, key=None, secret=None):
        """
        ApiKeyResponse - a model defined in Swagger
        """

        self._key = None
        self._secret = None

        self.key = key
        self.secret = secret

    @property
    def key(self):
        """
        Gets the key of this ApiKeyResponse.

        :return: The key of this ApiKeyResponse.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ApiKeyResponse.

        :param key: The key of this ApiKeyResponse.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def secret(self):
        """
        Gets the secret of this ApiKeyResponse.

        :return: The secret of this ApiKeyResponse.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this ApiKeyResponse.

        :param secret: The secret of this ApiKeyResponse.
        :type: str
        """
        if secret is None:
            raise ValueError("Invalid value for `secret`, must not be `None`")

        self._secret = secret

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ApiKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
