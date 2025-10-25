# AccountLinkResponsePkce


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_challenge** | **str** |  | 
**code_challenge_method** | **str** |  | 

## Example

```python
from openapi_client.models.account_link_response_pkce import AccountLinkResponsePkce

# TODO update the JSON string below
json = "{}"
# create an instance of AccountLinkResponsePkce from a JSON string
account_link_response_pkce_instance = AccountLinkResponsePkce.from_json(json)
# print the JSON string representation of the object
print(AccountLinkResponsePkce.to_json())

# convert the object into a dict
account_link_response_pkce_dict = account_link_response_pkce_instance.to_dict()
# create an instance of AccountLinkResponsePkce from a dict
account_link_response_pkce_from_dict = AccountLinkResponsePkce.from_dict(account_link_response_pkce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


