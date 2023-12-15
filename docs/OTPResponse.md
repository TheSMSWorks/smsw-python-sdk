# OTPResponse

Response schema for the /otp/send method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messageid** | **str** | The messageid of the SMS used to send the OTP. Save this in your application to use when verifying passcodes. | [optional] 
**status** | **str** | The initial status of the OTP message. | [optional] 
**credits** | **float** | The credit balance on your account | [optional] 
**credits_used** | **float** | The number of credits used to send this message | [optional] 
**messageparts** | **float** | The number of message parts used to send this message | [optional] 

## Example

```python
from openapi_client.models.otp_response import OTPResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OTPResponse from a JSON string
otp_response_instance = OTPResponse.from_json(json)
# print the JSON string representation of the object
print OTPResponse.to_json()

# convert the object into a dict
otp_response_dict = otp_response_instance.to_dict()
# create an instance of OTPResponse from a dict
otp_response_form_dict = otp_response.from_dict(otp_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


