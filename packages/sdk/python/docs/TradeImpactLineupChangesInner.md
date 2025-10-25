# TradeImpactLineupChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slot** | **str** |  | 
**in_player_id** | **str** | Canonical UUID identifier. | 
**out_player_id** | **str** | Canonical UUID identifier. | 

## Example

```python
from openapi_client.models.trade_impact_lineup_changes_inner import TradeImpactLineupChangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TradeImpactLineupChangesInner from a JSON string
trade_impact_lineup_changes_inner_instance = TradeImpactLineupChangesInner.from_json(json)
# print the JSON string representation of the object
print(TradeImpactLineupChangesInner.to_json())

# convert the object into a dict
trade_impact_lineup_changes_inner_dict = trade_impact_lineup_changes_inner_instance.to_dict()
# create an instance of TradeImpactLineupChangesInner from a dict
trade_impact_lineup_changes_inner_from_dict = TradeImpactLineupChangesInner.from_dict(trade_impact_lineup_changes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


