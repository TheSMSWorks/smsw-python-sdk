# coding: utf-8

"""
    The SMS Works API

    The SMS Works provides a low-cost, reliable SMS API for developers. Pay only for delivered texts, all failed UK messages are refunded.

    The version of the OpenAPI document: 1.9.0
    Contact: support@thesmsworks.co.uk
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.scheduled_messages_response_message import ScheduledMessagesResponseMessage

class TestScheduledMessagesResponseMessage(unittest.TestCase):
    """ScheduledMessagesResponseMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduledMessagesResponseMessage:
        """Test ScheduledMessagesResponseMessage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduledMessagesResponseMessage`
        """
        model = ScheduledMessagesResponseMessage()
        if include_optional:
            return ScheduledMessagesResponseMessage(
                var_schema = openapi_client.models.scheduled_message.ScheduledMessage(
                    sender = 'YourCompany', 
                    content = 'My super awesome scheduled message', 
                    destination = '447777777777', 
                    destinations = ["447777777777","447777777778","447777777779"], 
                    schedule = 'Wed Jul 19 2017 20:26:28 GMT+0100 (BST)', )
            )
        else:
            return ScheduledMessagesResponseMessage(
        )
        """

    def testScheduledMessagesResponseMessage(self):
        """Test ScheduledMessagesResponseMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
