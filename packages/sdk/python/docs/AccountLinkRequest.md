# AccountLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uri** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.account_link_request import AccountLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountLinkRequest from a JSON string
account_link_request_instance = AccountLinkRequest.from_json(json)
# print the JSON string representation of the object
print(AccountLinkRequest.to_json())

# convert the object into a dict
account_link_request_dict = account_link_request_instance.to_dict()
# create an instance of AccountLinkRequest from a dict
account_link_request_from_dict = AccountLinkRequest.from_dict(account_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


