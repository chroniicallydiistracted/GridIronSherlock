# TradeEstimateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league_id** | **str** | Canonical UUID identifier. | 
**period** | [**ScoringPeriod**](ScoringPeriod.md) |  | [optional] 
**from_team_id** | **str** | Canonical UUID identifier. | 
**to_team_id** | **str** | Canonical UUID identifier. | 
**offer** | [**List[TradeAsset]**](TradeAsset.md) |  | 
**request** | [**List[TradeAsset]**](TradeAsset.md) |  | 
**allow_counter** | **bool** |  | [optional] [default to True]
**include_waiver_alternatives** | **bool** |  | [optional] [default to False]

## Example

```python
from openapi_client.models.trade_estimate_request import TradeEstimateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TradeEstimateRequest from a JSON string
trade_estimate_request_instance = TradeEstimateRequest.from_json(json)
# print the JSON string representation of the object
print(TradeEstimateRequest.to_json())

# convert the object into a dict
trade_estimate_request_dict = trade_estimate_request_instance.to_dict()
# create an instance of TradeEstimateRequest from a dict
trade_estimate_request_from_dict = TradeEstimateRequest.from_dict(trade_estimate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


