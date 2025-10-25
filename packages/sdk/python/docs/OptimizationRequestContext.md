# OptimizationRequestContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_waivers** | **bool** |  | [optional] [default to False]
**include_trades** | **bool** |  | [optional] [default to False]
**notes** | **str** |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.optimization_request_context import OptimizationRequestContext

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationRequestContext from a JSON string
optimization_request_context_instance = OptimizationRequestContext.from_json(json)
# print the JSON string representation of the object
print(OptimizationRequestContext.to_json())

# convert the object into a dict
optimization_request_context_dict = optimization_request_context_instance.to_dict()
# create an instance of OptimizationRequestContext from a dict
optimization_request_context_from_dict = OptimizationRequestContext.from_dict(optimization_request_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


