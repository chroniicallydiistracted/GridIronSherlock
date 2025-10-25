# LeagueDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | [**LeagueSummary**](LeagueSummary.md) |  | 
**teams** | [**List[TeamReference]**](TeamReference.md) |  | 
**standings** | [**List[TeamStanding]**](TeamStanding.md) |  | [optional] 
**scoring** | [**LeagueDetailScoring**](LeagueDetailScoring.md) |  | 
**roster_settings** | [**LeagueDetailRosterSettings**](LeagueDetailRosterSettings.md) |  | [optional] 
**provenance** | [**Provenance**](Provenance.md) |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.league_detail import LeagueDetail

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueDetail from a JSON string
league_detail_instance = LeagueDetail.from_json(json)
# print the JSON string representation of the object
print(LeagueDetail.to_json())

# convert the object into a dict
league_detail_dict = league_detail_instance.to_dict()
# create an instance of LeagueDetail from a dict
league_detail_from_dict = LeagueDetail.from_dict(league_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


