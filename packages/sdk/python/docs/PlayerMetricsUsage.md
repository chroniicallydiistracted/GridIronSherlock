# PlayerMetricsUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_share** | **float** |  | [optional] 
**route_share** | **float** |  | [optional] 
**target_share** | **float** |  | [optional] 
**rush_share** | **float** |  | [optional] 
**red_zone_touch_share** | **float** |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.player_metrics_usage import PlayerMetricsUsage

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerMetricsUsage from a JSON string
player_metrics_usage_instance = PlayerMetricsUsage.from_json(json)
# print the JSON string representation of the object
print(PlayerMetricsUsage.to_json())

# convert the object into a dict
player_metrics_usage_dict = player_metrics_usage_instance.to_dict()
# create an instance of PlayerMetricsUsage from a dict
player_metrics_usage_from_dict = PlayerMetricsUsage.from_dict(player_metrics_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


