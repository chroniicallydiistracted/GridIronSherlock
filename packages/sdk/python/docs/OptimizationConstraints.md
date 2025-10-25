# OptimizationConstraints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locked_players** | [**List[OptimizationConstraintsLockedPlayersInner]**](OptimizationConstraintsLockedPlayersInner.md) |  | [optional] 
**excluded_player_ids** | **List[str]** |  | [optional] 
**max_players_per_team** | **int** |  | [optional] 
**risk_tolerance** | **str** |  | [optional] [default to 'medium']
**bench_depth** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.optimization_constraints import OptimizationConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationConstraints from a JSON string
optimization_constraints_instance = OptimizationConstraints.from_json(json)
# print the JSON string representation of the object
print(OptimizationConstraints.to_json())

# convert the object into a dict
optimization_constraints_dict = optimization_constraints_instance.to_dict()
# create an instance of OptimizationConstraints from a dict
optimization_constraints_from_dict = OptimizationConstraints.from_dict(optimization_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


