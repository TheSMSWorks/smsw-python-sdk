# OTP

Parameters for the generation and sending of One-Time Passwords

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | **str** | The sender of the message. Should be no longer than 11 characters for alphanumeric or 15 characters for numeric sender ID&#39;s. No spaces or special characters. | [optional] 
**destination** | **str** | The phone number of the recipient. | [optional] 
**length** | **object** | The length of the generated passcode. The default length is 6 characters, which will apply if this parameter is omitted. All generated passcodes are numeric. Optional. | [optional] 
**template** | **str** | A template to use as the content for the message. You must include the &#39;{{passcode}}&#39; placeholder, which will be replaced by the generated passcode when the message is sent. Optional. | [optional] 
**validity** | **float** | The length of time in seconds for which the generated passcode should be valid. Optional. | [optional] 
**passcode** | **str** | A passcode you supply for use in the message template. This will be stored on the OTP record in our system for later verification. Optional. | [optional] 
**metadata** | **object** | A JSON object of no longer than 1024 bytes, containing as many parameters as you wish, to store data for use in your application. This will be returned when you verify the passcode. | [optional] 

## Example

```python
from openapi_client.models.otp import OTP

# TODO update the JSON string below
json = "{}"
# create an instance of OTP from a JSON string
otp_instance = OTP.from_json(json)
# print the JSON string representation of the object
print OTP.to_json()

# convert the object into a dict
otp_dict = otp_instance.to_dict()
# create an instance of OTP from a dict
otp_form_dict = otp.from_dict(otp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


