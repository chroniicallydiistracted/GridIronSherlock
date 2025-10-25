# LiveImpactEventAffectedPlayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_id** | **str** | Canonical UUID identifier. | 
**team** | **str** |  | 
**impact** | **str** |  | [optional] 
**points_delta** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.live_impact_event_affected_players_inner import LiveImpactEventAffectedPlayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of LiveImpactEventAffectedPlayersInner from a JSON string
live_impact_event_affected_players_inner_instance = LiveImpactEventAffectedPlayersInner.from_json(json)
# print the JSON string representation of the object
print(LiveImpactEventAffectedPlayersInner.to_json())

# convert the object into a dict
live_impact_event_affected_players_inner_dict = live_impact_event_affected_players_inner_instance.to_dict()
# create an instance of LiveImpactEventAffectedPlayersInner from a dict
live_impact_event_affected_players_inner_from_dict = LiveImpactEventAffectedPlayersInner.from_dict(live_impact_event_affected_players_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


