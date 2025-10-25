# RecentGame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**week** | **int** |  | 
**opponent** | **str** |  | 
**fantasy_points** | **float** |  | [optional] 
**snap_share** | **float** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.recent_game import RecentGame

# TODO update the JSON string below
json = "{}"
# create an instance of RecentGame from a JSON string
recent_game_instance = RecentGame.from_json(json)
# print the JSON string representation of the object
print(RecentGame.to_json())

# convert the object into a dict
recent_game_dict = recent_game_instance.to_dict()
# create an instance of RecentGame from a dict
recent_game_from_dict = RecentGame.from_dict(recent_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


