# LeagueDetailRosterSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slots** | [**List[RosterSlotRule]**](RosterSlotRule.md) |  | 
**bench_slots** | **int** |  | 
**ir_slots** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.league_detail_roster_settings import LeagueDetailRosterSettings

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueDetailRosterSettings from a JSON string
league_detail_roster_settings_instance = LeagueDetailRosterSettings.from_json(json)
# print the JSON string representation of the object
print(LeagueDetailRosterSettings.to_json())

# convert the object into a dict
league_detail_roster_settings_dict = league_detail_roster_settings_instance.to_dict()
# create an instance of LeagueDetailRosterSettings from a dict
league_detail_roster_settings_from_dict = LeagueDetailRosterSettings.from_dict(league_detail_roster_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


