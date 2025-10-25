# TradeImpact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** | Canonical UUID identifier. | 
**projected_delta** | **float** |  | 
**risk_delta** | **float** |  | [optional] 
**lineup_changes** | [**List[TradeImpactLineupChangesInner]**](TradeImpactLineupChangesInner.md) |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.trade_impact import TradeImpact

# TODO update the JSON string below
json = "{}"
# create an instance of TradeImpact from a JSON string
trade_impact_instance = TradeImpact.from_json(json)
# print the JSON string representation of the object
print(TradeImpact.to_json())

# convert the object into a dict
trade_impact_dict = trade_impact_instance.to_dict()
# create an instance of TradeImpact from a dict
trade_impact_from_dict = TradeImpact.from_dict(trade_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


