# TradeEstimateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fairness_score** | **float** |  | 
**recommended_action** | **str** |  | 
**summary** | **str** |  | [optional] 
**team_impacts** | [**List[TradeImpact]**](TradeImpact.md) |  | 
**replacement_impact** | [**TradeEstimateResponseReplacementImpact**](TradeEstimateResponseReplacementImpact.md) |  | [optional] 
**warnings** | **List[str]** |  | [optional] 
**provenance** | [**Provenance**](Provenance.md) |  | 

## Example

```python
from openapi_client.models.trade_estimate_response import TradeEstimateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TradeEstimateResponse from a JSON string
trade_estimate_response_instance = TradeEstimateResponse.from_json(json)
# print the JSON string representation of the object
print(TradeEstimateResponse.to_json())

# convert the object into a dict
trade_estimate_response_dict = trade_estimate_response_instance.to_dict()
# create an instance of TradeEstimateResponse from a dict
trade_estimate_response_from_dict = TradeEstimateResponse.from_dict(trade_estimate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


