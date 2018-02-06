# swagger_client.UtilsApi

All URIs are relative to *https://api.thesmsworks.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hello**](UtilsApi.md#hello) | **GET** /utils/hello | 


# **hello**
> HelloWorldResponse hello(name=name)



Returns 'Hello' to the caller

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilsApi()
name = 'name_example' # str | The name of the person to whom to say hello (optional)

try: 
    api_response = api_instance.hello(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->hello: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the person to whom to say hello | [optional] 

### Return type

[**HelloWorldResponse**](HelloWorldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

