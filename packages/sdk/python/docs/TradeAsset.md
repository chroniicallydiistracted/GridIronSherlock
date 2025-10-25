# TradeAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**team_id** | **str** | Canonical UUID identifier. | 
**description** | **str** |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.trade_asset import TradeAsset

# TODO update the JSON string below
json = "{}"
# create an instance of TradeAsset from a JSON string
trade_asset_instance = TradeAsset.from_json(json)
# print the JSON string representation of the object
print(TradeAsset.to_json())

# convert the object into a dict
trade_asset_dict = trade_asset_instance.to_dict()
# create an instance of TradeAsset from a dict
trade_asset_from_dict = TradeAsset.from_dict(trade_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


