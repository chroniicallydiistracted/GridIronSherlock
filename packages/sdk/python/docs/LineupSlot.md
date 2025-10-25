# LineupSlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slot** | **str** |  | 
**player** | [**PlayerSummary**](PlayerSummary.md) |  | 
**projected** | [**ProjectionSummary**](ProjectionSummary.md) |  | 
**status** | **str** |  | [optional] [default to 'starting']
**actual_points** | **float** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.lineup_slot import LineupSlot

# TODO update the JSON string below
json = "{}"
# create an instance of LineupSlot from a JSON string
lineup_slot_instance = LineupSlot.from_json(json)
# print the JSON string representation of the object
print(LineupSlot.to_json())

# convert the object into a dict
lineup_slot_dict = lineup_slot_instance.to_dict()
# create an instance of LineupSlot from a dict
lineup_slot_from_dict = LineupSlot.from_dict(lineup_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


