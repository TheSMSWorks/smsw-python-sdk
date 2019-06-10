# Query

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the messages you would like returned (either &#x27;SENT&#x27;, &#x27;DELIVERED&#x27;, &#x27;EXPIRED&#x27;, &#x27;DELETED&#x27;, &#x27;UNDELIVERABLE&#x27;, &#x27;ACCEPTED&#x27;, &#x27;UNKNOWN&#x27;, &#x27;REJECTED&#x27;) | [optional] 
**destination** | **str** | The phone number of the recipient. Start UK numbers with 44 and drop the leading 0. | [optional] 
**sender** | **str** | The sender of the message (this can be the configured sender name for an outbound message or the senders phone number for an inbound message). | [optional] 
**keyword** | **str** | The keyword used in the inbound message | [optional] 
**_from** | **str** | The date-time from which you would like matching messages | [optional] 
**to** | **str** | The date-time to which you would like matching messages | [optional] 
**metadata** | **object** | An array of objects containing metadata key/value pairs that have been saved on messages. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

