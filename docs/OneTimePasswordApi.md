# openapi_client.OneTimePasswordApi

All URIs are relative to *https://api.thesmsworks.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otp_messageid_get**](OneTimePasswordApi.md#otp_messageid_get) | **GET** /otp/{messageid} | 
[**otp_send_post**](OneTimePasswordApi.md#otp_send_post) | **POST** /otp/send | 
[**otp_verify_post**](OneTimePasswordApi.md#otp_verify_post) | **POST** /otp/verify | 


# **otp_messageid_get**
> OTPVerifyResponse otp_messageid_get(messageid)



Retrieve an OTP by it's message ID

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import openapi_client
from openapi_client.models.otp_verify_response import OTPVerifyResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thesmsworks.co.uk/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.thesmsworks.co.uk/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OneTimePasswordApi(api_client)
    messageid = 'messageid_example' # str | The ID of the OTP you would like returned

    try:
        api_response = api_instance.otp_messageid_get(messageid)
        print("The response of OneTimePasswordApi->otp_messageid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OneTimePasswordApi->otp_messageid_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **messageid** | **str**| The ID of the OTP you would like returned | 

### Return type

[**OTPVerifyResponse**](OTPVerifyResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **otp_send_post**
> OTPResponse otp_send_post(otp)



Generates and sends a One-Time Password

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import openapi_client
from openapi_client.models.otp import OTP
from openapi_client.models.otp_response import OTPResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thesmsworks.co.uk/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.thesmsworks.co.uk/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OneTimePasswordApi(api_client)
    otp = openapi_client.OTP() # OTP | OTP properties

    try:
        api_response = api_instance.otp_send_post(otp)
        print("The response of OneTimePasswordApi->otp_send_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OneTimePasswordApi->otp_send_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otp** | [**OTP**](OTP.md)| OTP properties | 

### Return type

[**OTPResponse**](OTPResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **otp_verify_post**
> OTPVerifyResponse otp_verify_post(passcode)



Generates and sends a One-Time Password

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import openapi_client
from openapi_client.models.otp_verify import OTPVerify
from openapi_client.models.otp_verify_response import OTPVerifyResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thesmsworks.co.uk/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.thesmsworks.co.uk/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OneTimePasswordApi(api_client)
    passcode = openapi_client.OTPVerify() # OTPVerify | One-Time Password

    try:
        api_response = api_instance.otp_verify_post(passcode)
        print("The response of OneTimePasswordApi->otp_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OneTimePasswordApi->otp_verify_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **passcode** | [**OTPVerify**](OTPVerify.md)| One-Time Password | 

### Return type

[**OTPVerifyResponse**](OTPVerifyResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

