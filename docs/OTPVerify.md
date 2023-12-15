# OTPVerify

Schema for the /oyp/verify method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passcode** | **str** | One-Time Passcode submitted to your application | [optional] 

## Example

```python
from openapi_client.models.otp_verify import OTPVerify

# TODO update the JSON string below
json = "{}"
# create an instance of OTPVerify from a JSON string
otp_verify_instance = OTPVerify.from_json(json)
# print the JSON string representation of the object
print OTPVerify.to_json()

# convert the object into a dict
otp_verify_dict = otp_verify_instance.to_dict()
# create an instance of OTPVerify from a dict
otp_verify_form_dict = otp_verify.from_dict(otp_verify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


