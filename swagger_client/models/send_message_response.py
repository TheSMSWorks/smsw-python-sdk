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


class SendMessageResponse(object):
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
        'messageid': 'str',
        'status': 'str',
        'credits': 'int'
    }

    attribute_map = {
        'messageid': 'messageid',
        'status': 'status',
        'credits': 'credits'
    }

    def __init__(self, messageid=None, status=None, credits=None):
        """
        SendMessageResponse - a model defined in Swagger
        """

        self._messageid = None
        self._status = None
        self._credits = None

        self.messageid = messageid
        self.status = status
        self.credits = credits

    @property
    def messageid(self):
        """
        Gets the messageid of this SendMessageResponse.

        :return: The messageid of this SendMessageResponse.
        :rtype: str
        """
        return self._messageid

    @messageid.setter
    def messageid(self, messageid):
        """
        Sets the messageid of this SendMessageResponse.

        :param messageid: The messageid of this SendMessageResponse.
        :type: str
        """
        if messageid is None:
            raise ValueError("Invalid value for `messageid`, must not be `None`")

        self._messageid = messageid

    @property
    def status(self):
        """
        Gets the status of this SendMessageResponse.

        :return: The status of this SendMessageResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SendMessageResponse.

        :param status: The status of this SendMessageResponse.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def credits(self):
        """
        Gets the credits of this SendMessageResponse.

        :return: The credits of this SendMessageResponse.
        :rtype: int
        """
        return self._credits

    @credits.setter
    def credits(self, credits):
        """
        Sets the credits of this SendMessageResponse.

        :param credits: The credits of this SendMessageResponse.
        :type: int
        """
        if credits is None:
            raise ValueError("Invalid value for `credits`, must not be `None`")

        self._credits = credits

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
        if not isinstance(other, SendMessageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
