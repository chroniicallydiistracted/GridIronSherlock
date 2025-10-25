# OptimizationSlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slot** | **str** |  | 
**player** | [**PlayerSummary**](PlayerSummary.md) |  | 
**projection** | [**ProjectionSummary**](ProjectionSummary.md) |  | 
**delta** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.optimization_slot import OptimizationSlot

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationSlot from a JSON string
optimization_slot_instance = OptimizationSlot.from_json(json)
# print the JSON string representation of the object
print(OptimizationSlot.to_json())

# convert the object into a dict
optimization_slot_dict = optimization_slot_instance.to_dict()
# create an instance of OptimizationSlot from a dict
optimization_slot_from_dict = OptimizationSlot.from_dict(optimization_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


