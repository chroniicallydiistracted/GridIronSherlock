# OptimizationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | Canonical UUID identifier. | 
**submitted_at** | **datetime** |  | 
**objective** | [**OptimizationObjective**](OptimizationObjective.md) |  | 
**result_lineup** | [**List[OptimizationSlot]**](OptimizationSlot.md) |  | 
**bench** | [**List[OptimizationSlot]**](OptimizationSlot.md) |  | 
**alternatives** | [**List[OptimizationAlternative]**](OptimizationAlternative.md) |  | [optional] 
**insights** | **List[str]** |  | [optional] 
**provenance** | [**Provenance**](Provenance.md) |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.optimization_response import OptimizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationResponse from a JSON string
optimization_response_instance = OptimizationResponse.from_json(json)
# print the JSON string representation of the object
print(OptimizationResponse.to_json())

# convert the object into a dict
optimization_response_dict = optimization_response_instance.to_dict()
# create an instance of OptimizationResponse from a dict
optimization_response_from_dict = OptimizationResponse.from_dict(optimization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


