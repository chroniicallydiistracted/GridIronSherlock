# PlayerMetricsContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pace_rank** | **int** |  | [optional] 
**proe** | **float** |  | [optional] 
**matchup_difficulty** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.player_metrics_context import PlayerMetricsContext

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerMetricsContext from a JSON string
player_metrics_context_instance = PlayerMetricsContext.from_json(json)
# print the JSON string representation of the object
print(PlayerMetricsContext.to_json())

# convert the object into a dict
player_metrics_context_dict = player_metrics_context_instance.to_dict()
# create an instance of PlayerMetricsContext from a dict
player_metrics_context_from_dict = PlayerMetricsContext.from_dict(player_metrics_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


