# LeagueDetailScoring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**ppr** | **float** |  | 
**bonus_rules** | **List[str]** |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.league_detail_scoring import LeagueDetailScoring

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueDetailScoring from a JSON string
league_detail_scoring_instance = LeagueDetailScoring.from_json(json)
# print the JSON string representation of the object
print(LeagueDetailScoring.to_json())

# convert the object into a dict
league_detail_scoring_dict = league_detail_scoring_instance.to_dict()
# create an instance of LeagueDetailScoring from a dict
league_detail_scoring_from_dict = LeagueDetailScoring.from_dict(league_detail_scoring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


