# swagger_client.MessagesApi

All URIs are relative to *https://api.thesmsworks.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_scheduled_job**](MessagesApi.md#cancel_scheduled_job) | **DELETE** /messages/schedule/{messageid} | 
[**get_inbox_messages**](MessagesApi.md#get_inbox_messages) | **POST** /messages/inbox | 
[**get_message_by_id**](MessagesApi.md#get_message_by_id) | **GET** /messages/{messageid} | 
[**get_messages**](MessagesApi.md#get_messages) | **POST** /messages | 
[**schedule_message**](MessagesApi.md#schedule_message) | **POST** /message/schedule | 
[**send_message**](MessagesApi.md#send_message) | **POST** /message/send | 


# **cancel_scheduled_job**
> CancelledMessageResponse cancel_scheduled_job(messageid)



Cancels a scheduled SMS message

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
messageid = 'messageid_example' # str | The ID of the message you would like returned

try:
    api_response = api_instance.cancel_scheduled_job(messageid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->cancel_scheduled_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **messageid** | **str**| The ID of the message you would like returned | 

### Return type

[**CancelledMessageResponse**](CancelledMessageResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbox_messages**
> MessagesResponse get_inbox_messages(query)



Get unread uncoming messages matching your search criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
query = swagger_client.Query() # Query | 

try:
    api_response = api_instance.get_inbox_messages(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->get_inbox_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)|  | 

### Return type

[**MessagesResponse**](MessagesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_by_id**
> MessageResponse get_message_by_id(messageid)



Retrieve a logged message by the message ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
messageid = 'messageid_example' # str | The ID of the message you would like returned

try:
    api_response = api_instance.get_message_by_id(messageid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->get_message_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **messageid** | **str**| The ID of the message you would like returned | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> MessagesResponse get_messages(query)



Get messages matching your search criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
query = swagger_client.Query() # Query | 

try:
    api_response = api_instance.get_messages(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->get_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)|  | 

### Return type

[**MessagesResponse**](MessagesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_message**
> ScheduledMessageResponse schedule_message(sms_message)



Schedules an SMS message to be sent at the date-time you specify

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
sms_message = swagger_client.Message() # Message | Message properties

try:
    api_response = api_instance.schedule_message(sms_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->schedule_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_message** | [**Message**](Message.md)| Message properties | 

### Return type

[**ScheduledMessageResponse**](ScheduledMessageResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> SendMessageResponse send_message(sms_message)



Sends an SMS message

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
sms_message = swagger_client.Message() # Message | Message properties

try:
    api_response = api_instance.send_message(sms_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_message** | [**Message**](Message.md)| Message properties | 

### Return type

[**SendMessageResponse**](SendMessageResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

