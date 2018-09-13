# swagger_client.UtilsApi

All URIs are relative to *https://api.thesmsworks.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test**](UtilsApi.md#test) | **GET** /utils/test | 


# **test**
> TestResponse test()



Returns the customer ID to the caller

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilsApi()

try:
    api_response = api_instance.test()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->test: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TestResponse**](TestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

