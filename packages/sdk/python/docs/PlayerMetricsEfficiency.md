# PlayerMetricsEfficiency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yprr** | **float** |  | [optional] 
**adot** | **float** |  | [optional] 
**epa_per_target** | **float** |  | [optional] 
**epa_per_rush** | **float** |  | [optional] 
**success_rate** | **float** |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.player_metrics_efficiency import PlayerMetricsEfficiency

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerMetricsEfficiency from a JSON string
player_metrics_efficiency_instance = PlayerMetricsEfficiency.from_json(json)
# print the JSON string representation of the object
print(PlayerMetricsEfficiency.to_json())

# convert the object into a dict
player_metrics_efficiency_dict = player_metrics_efficiency_instance.to_dict()
# create an instance of PlayerMetricsEfficiency from a dict
player_metrics_efficiency_from_dict = PlayerMetricsEfficiency.from_dict(player_metrics_efficiency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


