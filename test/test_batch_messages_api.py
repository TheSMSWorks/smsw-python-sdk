# coding: utf-8

"""
    The SMS Works API

    The SMS Works provides a low-cost, reliable SMS API for developers. Pay only for delivered texts, all failed messages are refunded.  # noqa: E501

    OpenAPI spec version: 1.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.batch_messages_api import BatchMessagesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBatchMessagesApi(unittest.TestCase):
    """BatchMessagesApi unit test stubs"""

    def setUp(self):
        self.api = api.batch_messages_api.BatchMessagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_scheduled_batch_job(self):
        """Test case for cancel_scheduled_batch_job

        """
        pass

    def test_get_batch_by_id(self):
        """Test case for get_batch_by_id

        """
        pass

    def test_schedule_batch(self):
        """Test case for schedule_batch

        """
        pass

    def test_send_batch(self):
        """Test case for send_batch

        """
        pass


if __name__ == '__main__':
    unittest.main()
