# PlayerListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 
**items** | [**List[PlayerSummary]**](PlayerSummary.md) |  | 

## Example

```python
from openapi_client.models.player_list_response import PlayerListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerListResponse from a JSON string
player_list_response_instance = PlayerListResponse.from_json(json)
# print the JSON string representation of the object
print(PlayerListResponse.to_json())

# convert the object into a dict
player_list_response_dict = player_list_response_instance.to_dict()
# create an instance of PlayerListResponse from a dict
player_list_response_from_dict = PlayerListResponse.from_dict(player_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


