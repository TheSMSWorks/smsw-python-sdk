# swagger_client.BatchMessagesApi

All URIs are relative to *https://api.thesmsworks.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_scheduled_batch_job**](BatchMessagesApi.md#cancel_scheduled_batch_job) | **DELETE** /batches/schedule/{batchid} | 
[**get_batch_by_id**](BatchMessagesApi.md#get_batch_by_id) | **GET** /batch/{batchid} | 
[**schedule_batch**](BatchMessagesApi.md#schedule_batch) | **POST** /batch/schedule | 
[**send_batch**](BatchMessagesApi.md#send_batch) | **POST** /batch/send | 

# **cancel_scheduled_batch_job**
> CancelledMessageResponse cancel_scheduled_batch_job(batchid)



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
api_instance = swagger_client.BatchMessagesApi(swagger_client.ApiClient(configuration))
batchid = 'batchid_example' # str | The ID of the batch you would like returned

try:
    api_response = api_instance.cancel_scheduled_batch_job(batchid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchMessagesApi->cancel_scheduled_batch_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batchid** | **str**| The ID of the batch you would like returned | 

### Return type

[**CancelledMessageResponse**](CancelledMessageResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_by_id**
> list[MessageResponse] get_batch_by_id(batchid)



Retrieve all messages in a batch with the given batch ID

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
api_instance = swagger_client.BatchMessagesApi(swagger_client.ApiClient(configuration))
batchid = 'batchid_example' # str | The ID of the batch you would like returned

try:
    api_response = api_instance.get_batch_by_id(batchid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchMessagesApi->get_batch_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batchid** | **str**| The ID of the batch you would like returned | 

### Return type

[**list[MessageResponse]**](MessageResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_batch**
> ScheduledBatchResponse schedule_batch(body)



Schedules a batch of SMS messages to be sent at the date time you specify

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
api_instance = swagger_client.BatchMessagesApi(swagger_client.ApiClient(configuration))
body = swagger_client.BatchMessage() # BatchMessage | Message properties

try:
    api_response = api_instance.schedule_batch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchMessagesApi->schedule_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchMessage**](BatchMessage.md)| Message properties | 

### Return type

[**ScheduledBatchResponse**](ScheduledBatchResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_batch**
> BatchMessageResponse send_batch(body)



Send a single SMS message to multiple recipients

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
api_instance = swagger_client.BatchMessagesApi(swagger_client.ApiClient(configuration))
body = swagger_client.BatchMessage() # BatchMessage | Message properties

try:
    api_response = api_instance.send_batch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchMessagesApi->send_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchMessage**](BatchMessage.md)| Message properties | 

### Return type

[**BatchMessageResponse**](BatchMessageResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

