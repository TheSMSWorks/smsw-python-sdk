# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

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

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.AuthApi()
customerid = 'customerid_example' # str | The Customer ID

try:
    api_response = api_instance.key_secret(customerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->key_secret: %s\n" % e)

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
*MessagesApi* | [**cancel_scheduled_job**](docs/MessagesApi.md#cancel_scheduled_job) | **DELETE** /messages/schedule/{messageid} | 
*MessagesApi* | [**get_message_by_id**](docs/MessagesApi.md#get_message_by_id) | **GET** /messages/{messageid} | 
*MessagesApi* | [**get_messages**](docs/MessagesApi.md#get_messages) | **POST** /messages | 
*MessagesApi* | [**schedule_message**](docs/MessagesApi.md#schedule_message) | **POST** /message/schedule | 
*MessagesApi* | [**send_message**](docs/MessagesApi.md#send_message) | **POST** /message/send | 
*UtilsApi* | [**hello**](docs/UtilsApi.md#hello) | **GET** /utils/hello | 


## Documentation For Models

 - [ApiKeyResponse](docs/ApiKeyResponse.md)
 - [BatchMessage](docs/BatchMessage.md)
 - [BatchMessageResponse](docs/BatchMessageResponse.md)
 - [CancelledMessageResponse](docs/CancelledMessageResponse.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [HelloWorldResponse](docs/HelloWorldResponse.md)
 - [Login](docs/Login.md)
 - [Message](docs/Message.md)
 - [MessageResponse](docs/MessageResponse.md)
 - [MessagesResponse](docs/MessagesResponse.md)
 - [MessagesResponseMessages](docs/MessagesResponseMessages.md)
 - [Query](docs/Query.md)
 - [ScheduledBatchResponse](docs/ScheduledBatchResponse.md)
 - [ScheduledMessageResponse](docs/ScheduledMessageResponse.md)
 - [SendMessageResponse](docs/SendMessageResponse.md)
 - [TokenResponse](docs/TokenResponse.md)
 - [ExtendedErrorModel](docs/ExtendedErrorModel.md)


## Documentation For Authorization


## JWT

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Test calls in Postman

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/5348de8f62f83cddcee3)



