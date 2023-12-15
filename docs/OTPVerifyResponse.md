# OTPVerifyResponse

Response schema for the /otp/verify method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | The mobile number that the OTP was sent to | [optional] 
**status** | **str** | The status of the OTP. If the passcode is used within the validity period then this will be &#39;VERIFIED&#39;, otherwise it will be &#39;EXPIRED&#39; | [optional] 
**passcode** | **float** | The passcode used. | [optional] 
**validity** | **float** | The length of time in seconds for which the generated passcode is valid. | [optional] 
**metadata** | **object** | A JSON object storing data supplied when this passcode was generated, for use in your application. | [optional] 
**created** | **str** | The ISO 8601 date/time at which this OTP was created | [optional] 
**expires** | **str** | The ISO 8601 date/time at which this OTP expires | [optional] 
**modified** | **str** | The ISO 8601 date/time at which this OTP was modified (typically when it was verified) | [optional] 

## Example

```python
from openapi_client.models.otp_verify_response import OTPVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OTPVerifyResponse from a JSON string
otp_verify_response_instance = OTPVerifyResponse.from_json(json)
# print the JSON string representation of the object
print OTPVerifyResponse.to_json()

# convert the object into a dict
otp_verify_response_dict = otp_verify_response_instance.to_dict()
# create an instance of OTPVerifyResponse from a dict
otp_verify_response_form_dict = otp_verify_response.from_dict(otp_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


