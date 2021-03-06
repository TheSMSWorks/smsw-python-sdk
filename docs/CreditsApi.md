# swagger_client.CreditsApi

All URIs are relative to *https://api.thesmsworks.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credits**](CreditsApi.md#credits) | **GET** /credits/balance | 

# **credits**
> CreditsResponse credits()



Returns the number of credits currently available on the account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditsApi()

try:
    api_response = api_instance.credits()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditsApi->credits: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreditsResponse**](CreditsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

