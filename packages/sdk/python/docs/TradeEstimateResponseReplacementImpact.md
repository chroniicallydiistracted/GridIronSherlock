# TradeEstimateResponseReplacementImpact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** | Canonical UUID identifier. | [optional] 
**delta** | **float** |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.trade_estimate_response_replacement_impact import TradeEstimateResponseReplacementImpact

# TODO update the JSON string below
json = "{}"
# create an instance of TradeEstimateResponseReplacementImpact from a JSON string
trade_estimate_response_replacement_impact_instance = TradeEstimateResponseReplacementImpact.from_json(json)
# print the JSON string representation of the object
print(TradeEstimateResponseReplacementImpact.to_json())

# convert the object into a dict
trade_estimate_response_replacement_impact_dict = trade_estimate_response_replacement_impact_instance.to_dict()
# create an instance of TradeEstimateResponseReplacementImpact from a dict
trade_estimate_response_replacement_impact_from_dict = TradeEstimateResponseReplacementImpact.from_dict(trade_estimate_response_replacement_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


