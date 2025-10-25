# OptimizationAlternative


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** |  | 
**projected_points** | **float** |  | 
**delta_from_best** | **float** |  | [optional] 
**lineup** | [**List[OptimizationSlot]**](OptimizationSlot.md) |  | 
**changes** | [**List[OptimizationAlternativeChangesInner]**](OptimizationAlternativeChangesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.optimization_alternative import OptimizationAlternative

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationAlternative from a JSON string
optimization_alternative_instance = OptimizationAlternative.from_json(json)
# print the JSON string representation of the object
print(OptimizationAlternative.to_json())

# convert the object into a dict
optimization_alternative_dict = optimization_alternative_instance.to_dict()
# create an instance of OptimizationAlternative from a dict
optimization_alternative_from_dict = OptimizationAlternative.from_dict(optimization_alternative_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


