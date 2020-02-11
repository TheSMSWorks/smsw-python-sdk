# swagger-client
The SMS Works provides a low-cost, reliable SMS API for developers. Pay only for delivered texts, all failed messages are refunded.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.3.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/TheSMSWorks/smsw-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/TheSMSWorks/smsw-python-sdk.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Documentation for API Endpoints

All URIs are relative to *https://api.thesmsworks.co.uk/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**key_secret**](docs/AuthApi.md#key_secret) | **GET** /auth/getApiKey | 
*AuthApi* | [**login**](docs/AuthApi.md#login) | **POST** /auth/token | 
*BatchMessagesApi* | [**cancel_scheduled_batch_job**](docs/BatchMessagesApi.md#cancel_scheduled_batch_job) | **DELETE** /batches/schedule/{batchid} | 
*BatchMessagesApi* | [**get_batch_by_id**](docs/BatchMessagesApi.md#get_batch_by_id) | **GET** /batch/{batchid} | 
*BatchMessagesApi* | [**schedule_batch**](docs/BatchMessagesApi.md#schedule_batch) | **POST** /batch/schedule | 
*BatchMessagesApi* | [**send_batch**](docs/BatchMessagesApi.md#send_batch) | **POST** /batch/send | 
*CreditsApi* | [**credits**](docs/CreditsApi.md#credits) | **GET** /credits/balance | 
*MessagesApi* | [**cancel_scheduled_job**](docs/MessagesApi.md#cancel_scheduled_job) | **DELETE** /messages/schedule/{messageid} | 
*MessagesApi* | [**get_inbox_messages**](docs/MessagesApi.md#get_inbox_messages) | **POST** /messages/inbox | 
*MessagesApi* | [**get_message_by_id**](docs/MessagesApi.md#get_message_by_id) | **GET** /messages/{messageid} | 
*MessagesApi* | [**get_messages**](docs/MessagesApi.md#get_messages) | **POST** /messages | 
*MessagesApi* | [**schedule_message**](docs/MessagesApi.md#schedule_message) | **POST** /message/schedule | 
*MessagesApi* | [**send_message**](docs/MessagesApi.md#send_message) | **POST** /message/send | 
*UtilsApi* | [**get_error**](docs/UtilsApi.md#get_error) | **GET** /utils/errors/{errorcode} | 
*UtilsApi* | [**test**](docs/UtilsApi.md#test) | **GET** /utils/test | 

## Documentation For Models

 - [ApiKeyResponse](docs/ApiKeyResponse.md)
 - [BatchMessage](docs/BatchMessage.md)
 - [BatchMessageResponse](docs/BatchMessageResponse.md)
 - [CancelledMessageResponse](docs/CancelledMessageResponse.md)
 - [CreditsResponse](docs/CreditsResponse.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [ExtendedErrorModel](docs/ExtendedErrorModel.md)
 - [Login](docs/Login.md)
 - [Message](docs/Message.md)
 - [MessageResponse](docs/MessageResponse.md)
 - [MessagesResponse](docs/MessagesResponse.md)
 - [MetaData](docs/MetaData.md)
 - [Query](docs/Query.md)
 - [ScheduledBatchResponse](docs/ScheduledBatchResponse.md)
 - [ScheduledMessageResponse](docs/ScheduledMessageResponse.md)
 - [SendMessageResponse](docs/SendMessageResponse.md)
 - [TestResponse](docs/TestResponse.md)
 - [TokenResponse](docs/TokenResponse.md)

## Documentation For Authorization


## JWT

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


