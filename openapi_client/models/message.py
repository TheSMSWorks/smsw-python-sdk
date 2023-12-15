# coding: utf-8

"""
    The SMS Works API

    The SMS Works provides a low-cost, reliable SMS API for developers. Pay only for delivered texts, all failed UK messages are refunded.

    The version of the OpenAPI document: 1.9.0
    Contact: support@thesmsworks.co.uk
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from openapi_client.models.message_metadata import MessageMetadata
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Message(BaseModel):
    """
    SMS message object
    """ # noqa: E501
    sender: StrictStr = Field(description="The sender of the message. Should be no longer than 11 characters for alphanumeric or 15 characters for numeric sender ID's. No spaces or special characters.")
    destination: StrictStr = Field(description="Telephone number of the recipient")
    content: StrictStr = Field(description="Message to send to the recipient. Content can be up to 1280 characters in length. Messages of 160 characters or fewer are charged 1 credit. If your message is longer than 160 characters then it will be broken down in to chunks of 153 characters before being sent to the recipient's handset, and you will be charged 1 credit for each 153 characters. Messages sent to numbers registered outside the UK will be typically charged double credits, but for certain countries may be charged fractions of credits (e.g. 2.5). Please contact us for rates for each country.")
    deliveryreporturl: Optional[StrictStr] = Field(default=None, description="The url to which we should POST delivery reports to for this message. If none is specified, we'll use the global delivery report URL that you've configured on your account page.")
    schedule: Optional[StrictStr] = Field(default=None, description="Date at which to send the message. This is only used by the message/schedule service and can be left empty for other services.")
    tag: Optional[StrictStr] = Field(default=None, description="An identifying label for the message, which you can use to filter and report on messages you've sent later. Ideal for campaigns. A maximum of 280 characters.")
    ttl: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The optional number of minutes before the delivery report is deleted. Optional. Omit to prevent delivery report deletion. Integer.")
    responseemail: Optional[List[StrictStr]] = Field(default=None, description="An optional list of email addresses to forward responses to this specific message to. An SMS Works Reply Number is required to use this feature.")
    metadata: Optional[MessageMetadata] = None
    validity: Optional[Union[Annotated[float, Field(le=2880, strict=True, ge=1)], Annotated[int, Field(le=2880, strict=True, ge=1)]]] = Field(default=None, description="The optional number of minutes to attempt delivery before the message is marked as EXPIRED. Optional. The default is 2880 minutes. Integer.")
    ai: Optional[StrictBool] = Field(default=None, description="Used to determine whether The SMS Works AI Optimiser should be used in the event that the message is just longer than the 1 or 2 credit boundary. This setting overrides the AI Optimiser configuration on your SMS Works account.")
    __properties: ClassVar[List[str]] = ["sender", "destination", "content", "deliveryreporturl", "schedule", "tag", "ttl", "responseemail", "metadata", "validity", "ai"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Message from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Message from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sender": obj.get("sender"),
            "destination": obj.get("destination"),
            "content": obj.get("content"),
            "deliveryreporturl": obj.get("deliveryreporturl"),
            "schedule": obj.get("schedule"),
            "tag": obj.get("tag"),
            "ttl": obj.get("ttl"),
            "responseemail": obj.get("responseemail"),
            "metadata": MessageMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "validity": obj.get("validity"),
            "ai": obj.get("ai")
        })
        return _obj


