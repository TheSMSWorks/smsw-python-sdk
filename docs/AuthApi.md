# swagger_client.AuthApi

All URIs are relative to *https://api.thesmsworks.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**key_secret**](AuthApi.md#key_secret) | **GET** /auth/getApiKey | 
[**login**](AuthApi.md#login) | **POST** /auth/token | 

# **key_secret**
> ApiKeyResponse key_secret(customerid)



Utility method. Please generate your API key by following the instructions on your account page at https://thesmsworks.co.uk/user/login

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
customerid = 'customerid_example' # str | Utility method. Please generate your API key by following the instructions on your account page at https://thesmsworks.co.uk/user/login

try:
    api_response = api_instance.key_secret(customerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->key_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customerid** | **str**| Utility method. Please generate your API key by following the instructions on your account page at https://thesmsworks.co.uk/user/login | 

### Return type

[**ApiKeyResponse**](ApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> TokenResponse login(body)



Generates a JSON Web Token for including in the Authorization header of all your calls to the API. This only needs to be done once. Generate the customer ID, API Key & Secret required for this call from the API Key tab your account page.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.Login() # Login | API Key & Secret

try:
    api_response = api_instance.login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Login**](Login.md)| API Key &amp; Secret | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

