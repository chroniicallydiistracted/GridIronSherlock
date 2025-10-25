# PlayerDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**PlayerSummary**](PlayerSummary.md) |  | 
**metrics** | [**PlayerMetrics**](PlayerMetrics.md) |  | 
**projections** | [**PlayerDetailProjections**](PlayerDetailProjections.md) |  | 
**recent_games** | [**List[RecentGame]**](RecentGame.md) |  | [optional] 
**insights** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.player_detail import PlayerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerDetail from a JSON string
player_detail_instance = PlayerDetail.from_json(json)
# print the JSON string representation of the object
print(PlayerDetail.to_json())

# convert the object into a dict
player_detail_dict = player_detail_instance.to_dict()
# create an instance of PlayerDetail from a dict
player_detail_from_dict = PlayerDetail.from_dict(player_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


