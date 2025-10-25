# PlayerMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**week** | **int** |  | 
**usage** | [**PlayerMetricsUsage**](PlayerMetricsUsage.md) |  | [optional] 
**efficiency** | [**PlayerMetricsEfficiency**](PlayerMetricsEfficiency.md) |  | [optional] 
**context** | [**PlayerMetricsContext**](PlayerMetricsContext.md) |  | [optional] 
**provenance** | [**Provenance**](Provenance.md) |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.player_metrics import PlayerMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerMetrics from a JSON string
player_metrics_instance = PlayerMetrics.from_json(json)
# print the JSON string representation of the object
print(PlayerMetrics.to_json())

# convert the object into a dict
player_metrics_dict = player_metrics_instance.to_dict()
# create an instance of PlayerMetrics from a dict
player_metrics_from_dict = PlayerMetrics.from_dict(player_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


