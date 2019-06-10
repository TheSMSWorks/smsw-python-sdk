# coding: utf-8

"""
    The SMS Works API

    The SMS Works provides a low-cost, reliable SMS API for developers. Pay only for delivered texts, all failed messages are refunded.  # noqa: E501

    OpenAPI spec version: 1.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class BatchMessagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_scheduled_batch_job(self, batchid, **kwargs):  # noqa: E501
        """cancel_scheduled_batch_job  # noqa: E501

        Cancels a scheduled SMS message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_scheduled_batch_job(batchid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str batchid: The ID of the batch you would like returned (required)
        :return: CancelledMessageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_scheduled_batch_job_with_http_info(batchid, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_scheduled_batch_job_with_http_info(batchid, **kwargs)  # noqa: E501
            return data

    def cancel_scheduled_batch_job_with_http_info(self, batchid, **kwargs):  # noqa: E501
        """cancel_scheduled_batch_job  # noqa: E501

        Cancels a scheduled SMS message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_scheduled_batch_job_with_http_info(batchid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str batchid: The ID of the batch you would like returned (required)
        :return: CancelledMessageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batchid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_scheduled_batch_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batchid' is set
        if ('batchid' not in params or
                params['batchid'] is None):
            raise ValueError("Missing the required parameter `batchid` when calling `cancel_scheduled_batch_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'batchid' in params:
            path_params['batchid'] = params['batchid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/batches/schedule/{batchid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CancelledMessageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_batch_by_id(self, batchid, **kwargs):  # noqa: E501
        """get_batch_by_id  # noqa: E501

        Retrieve all messages in a batch with the given batch ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_batch_by_id(batchid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str batchid: The ID of the batch you would like returned (required)
        :return: MessagesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_batch_by_id_with_http_info(batchid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_batch_by_id_with_http_info(batchid, **kwargs)  # noqa: E501
            return data

    def get_batch_by_id_with_http_info(self, batchid, **kwargs):  # noqa: E501
        """get_batch_by_id  # noqa: E501

        Retrieve all messages in a batch with the given batch ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_batch_by_id_with_http_info(batchid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str batchid: The ID of the batch you would like returned (required)
        :return: MessagesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batchid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_batch_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batchid' is set
        if ('batchid' not in params or
                params['batchid'] is None):
            raise ValueError("Missing the required parameter `batchid` when calling `get_batch_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'batchid' in params:
            path_params['batchid'] = params['batchid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/batch/{batchid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessagesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schedule_batch(self, body, **kwargs):  # noqa: E501
        """schedule_batch  # noqa: E501

        Schedules a batch of SMS messages to be sent at the date time you specify  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedule_batch(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchMessage body: Message properties (required)
        :return: ScheduledBatchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedule_batch_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.schedule_batch_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def schedule_batch_with_http_info(self, body, **kwargs):  # noqa: E501
        """schedule_batch  # noqa: E501

        Schedules a batch of SMS messages to be sent at the date time you specify  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedule_batch_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchMessage body: Message properties (required)
        :return: ScheduledBatchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedule_batch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `schedule_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/batch/schedule', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScheduledBatchResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_batch(self, body, **kwargs):  # noqa: E501
        """send_batch  # noqa: E501

        Send a single SMS message to multiple recipients  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_batch(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchMessage body: Message properties (required)
        :return: BatchMessageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_batch_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.send_batch_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def send_batch_with_http_info(self, body, **kwargs):  # noqa: E501
        """send_batch  # noqa: E501

        Send a single SMS message to multiple recipients  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_batch_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchMessage body: Message properties (required)
        :return: BatchMessageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_batch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `send_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/batch/send', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchMessageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
