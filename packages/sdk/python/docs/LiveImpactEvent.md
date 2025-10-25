# LiveImpactEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** |  | 
**game_id** | **str** |  | 
**play_id** | **int** |  | 
**occurred_at** | **datetime** |  | 
**headline** | **str** |  | 
**description** | **str** |  | [optional] 
**impact_type** | **str** |  | 
**affected_players** | [**List[LiveImpactEventAffectedPlayersInner]**](LiveImpactEventAffectedPlayersInner.md) |  | [optional] 
**fantasy_implications** | **List[str]** |  | 
**provenance** | [**Provenance**](Provenance.md) |  | [optional] 
**links** | **List[str]** |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.live_impact_event import LiveImpactEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LiveImpactEvent from a JSON string
live_impact_event_instance = LiveImpactEvent.from_json(json)
# print the JSON string representation of the object
print(LiveImpactEvent.to_json())

# convert the object into a dict
live_impact_event_dict = live_impact_event_instance.to_dict()
# create an instance of LiveImpactEvent from a dict
live_impact_event_from_dict = LiveImpactEvent.from_dict(live_impact_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


