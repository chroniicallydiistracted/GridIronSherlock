# OptimizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**ScoringPeriod**](ScoringPeriod.md) |  | 
**objective** | [**OptimizationObjective**](OptimizationObjective.md) |  | 
**constraints** | [**OptimizationConstraints**](OptimizationConstraints.md) |  | [optional] 
**context** | [**OptimizationRequestContext**](OptimizationRequestContext.md) |  | [optional] 

## Example

```python
from openapi_client.models.optimization_request import OptimizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationRequest from a JSON string
optimization_request_instance = OptimizationRequest.from_json(json)
# print the JSON string representation of the object
print(OptimizationRequest.to_json())

# convert the object into a dict
optimization_request_dict = optimization_request_instance.to_dict()
# create an instance of OptimizationRequest from a dict
optimization_request_from_dict = OptimizationRequest.from_dict(optimization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


