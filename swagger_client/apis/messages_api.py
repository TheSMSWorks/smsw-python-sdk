# coding: utf-8

"""
    The SMS Works API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class MessagesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def cancel_scheduled_job(self, messageid, **kwargs):
        """
        Cancels a scheduled SMS message
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancel_scheduled_job(messageid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str messageid: The ID of the message you would like returned (required)
        :return: CancelledMessageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cancel_scheduled_job_with_http_info(messageid, **kwargs)
        else:
            (data) = self.cancel_scheduled_job_with_http_info(messageid, **kwargs)
            return data

    def cancel_scheduled_job_with_http_info(self, messageid, **kwargs):
        """
        Cancels a scheduled SMS message
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancel_scheduled_job_with_http_info(messageid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str messageid: The ID of the message you would like returned (required)
        :return: CancelledMessageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['messageid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_scheduled_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'messageid' is set
        if ('messageid' not in params) or (params['messageid'] is None):
            raise ValueError("Missing the required parameter `messageid` when calling `cancel_scheduled_job`")


        collection_formats = {}

        path_params = {}
        if 'messageid' in params:
            path_params['messageid'] = params['messageid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json;charset=UTF-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        return self.api_client.call_api('/messages/schedule/{messageid}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CancelledMessageResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_message_by_id(self, messageid, **kwargs):
        """
        Retrieve a logged message by the message ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_message_by_id(messageid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str messageid: The ID of the message you would like returned (required)
        :return: MessageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_message_by_id_with_http_info(messageid, **kwargs)
        else:
            (data) = self.get_message_by_id_with_http_info(messageid, **kwargs)
            return data

    def get_message_by_id_with_http_info(self, messageid, **kwargs):
        """
        Retrieve a logged message by the message ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_message_by_id_with_http_info(messageid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str messageid: The ID of the message you would like returned (required)
        :return: MessageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['messageid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_message_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'messageid' is set
        if ('messageid' not in params) or (params['messageid'] is None):
            raise ValueError("Missing the required parameter `messageid` when calling `get_message_by_id`")


        collection_formats = {}

        path_params = {}
        if 'messageid' in params:
            path_params['messageid'] = params['messageid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json;charset=UTF-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        return self.api_client.call_api('/messages/{messageid}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MessageResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_messages(self, query, **kwargs):
        """
        Get messages matching your search criteria
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_messages(query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Query query: (required)
        :return: MessagesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_messages_with_http_info(query, **kwargs)
        else:
            (data) = self.get_messages_with_http_info(query, **kwargs)
            return data

    def get_messages_with_http_info(self, query, **kwargs):
        """
        Get messages matching your search criteria
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_messages_with_http_info(query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Query query: (required)
        :return: MessagesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_messages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `get_messages`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query' in params:
            body_params = params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json;charset=UTF-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        return self.api_client.call_api('/messages', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MessagesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def schedule_message(self, sms_message, **kwargs):
        """
        Schedules an SMS message to be sent at the date-time you specify
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.schedule_message(sms_message, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Message sms_message: Message properties (required)
        :return: ScheduledMessageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.schedule_message_with_http_info(sms_message, **kwargs)
        else:
            (data) = self.schedule_message_with_http_info(sms_message, **kwargs)
            return data

    def schedule_message_with_http_info(self, sms_message, **kwargs):
        """
        Schedules an SMS message to be sent at the date-time you specify
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.schedule_message_with_http_info(sms_message, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Message sms_message: Message properties (required)
        :return: ScheduledMessageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sms_message']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedule_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sms_message' is set
        if ('sms_message' not in params) or (params['sms_message'] is None):
            raise ValueError("Missing the required parameter `sms_message` when calling `schedule_message`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sms_message' in params:
            body_params = params['sms_message']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json;charset=UTF-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        return self.api_client.call_api('/message/schedule', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ScheduledMessageResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def send_message(self, sms_message, **kwargs):
        """
        Sends an SMS message
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.send_message(sms_message, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Message sms_message: Message properties (required)
        :return: SendMessageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.send_message_with_http_info(sms_message, **kwargs)
        else:
            (data) = self.send_message_with_http_info(sms_message, **kwargs)
            return data

    def send_message_with_http_info(self, sms_message, **kwargs):
        """
        Sends an SMS message
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.send_message_with_http_info(sms_message, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Message sms_message: Message properties (required)
        :return: SendMessageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sms_message']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sms_message' is set
        if ('sms_message' not in params) or (params['sms_message'] is None):
            raise ValueError("Missing the required parameter `sms_message` when calling `send_message`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sms_message' in params:
            body_params = params['sms_message']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json;charset=UTF-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        return self.api_client.call_api('/message/send', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SendMessageResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)