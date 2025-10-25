# PlayerSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_id** | **str** |  | 
**gsis_id** | **str** |  | [optional] 
**full_name** | **str** |  | 
**position** | **str** |  | 
**team** | **str** |  | 
**bye_week** | **int** |  | [optional] 
**age** | **int** |  | [optional] 
**injury** | [**InjuryStatus**](InjuryStatus.md) |  | [optional] 
**provenance** | [**Provenance**](Provenance.md) |  | [optional] 

## Example

```python
from openapi_client.models.player_summary import PlayerSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSummary from a JSON string
player_summary_instance = PlayerSummary.from_json(json)
# print the JSON string representation of the object
print(PlayerSummary.to_json())

# convert the object into a dict
player_summary_dict = player_summary_instance.to_dict()
# create an instance of PlayerSummary from a dict
player_summary_from_dict = PlayerSummary.from_dict(player_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


