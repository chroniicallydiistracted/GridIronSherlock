# OptimizationObjective


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**focus** | **str** |  | 
**ceiling_weight** | **float** |  | [optional] [default to 0.5]
**variance_penalty** | **float** |  | [optional] [default to 0.25]
**notes** | **str** |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.optimization_objective import OptimizationObjective

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationObjective from a JSON string
optimization_objective_instance = OptimizationObjective.from_json(json)
# print the JSON string representation of the object
print(OptimizationObjective.to_json())

# convert the object into a dict
optimization_objective_dict = optimization_objective_instance.to_dict()
# create an instance of OptimizationObjective from a dict
optimization_objective_from_dict = OptimizationObjective.from_dict(optimization_objective_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


