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


class ErrorModel(object):
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
        'message': 'str',
        'code': 'int'
    }

    attribute_map = {
        'message': 'message',
        'code': 'code'
    }

    def __init__(self, message=None, code=None):
        """
        ErrorModel - a model defined in Swagger
        """

        self._message = None
        self._code = None

        self.message = message
        self.code = code

    @property
    def message(self):
        """
        Gets the message of this ErrorModel.

        :return: The message of this ErrorModel.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ErrorModel.

        :param message: The message of this ErrorModel.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def code(self):
        """
        Gets the code of this ErrorModel.

        :return: The code of this ErrorModel.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ErrorModel.

        :param code: The code of this ErrorModel.
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")
        if code is not None and code > 600:
            raise ValueError("Invalid value for `code`, must be a value less than or equal to `600`")
        if code is not None and code < 100:
            raise ValueError("Invalid value for `code`, must be a value greater than or equal to `100`")

        self._code = code

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
        if not isinstance(other, ErrorModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
