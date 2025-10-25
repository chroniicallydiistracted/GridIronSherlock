# TeamLineupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | [**TeamReference**](TeamReference.md) |  | 
**period** | [**ScoringPeriod**](ScoringPeriod.md) |  | 
**lineup** | [**List[LineupSlot]**](LineupSlot.md) |  | 
**bench** | [**List[LineupSlot]**](LineupSlot.md) |  | 
**total_projected** | **float** |  | [optional] 
**total_actual** | **float** |  | [optional] 
**provenance** | [**Provenance**](Provenance.md) |  | [optional] 

## Example

```python
from openapi_client.models.team_lineup_response import TeamLineupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TeamLineupResponse from a JSON string
team_lineup_response_instance = TeamLineupResponse.from_json(json)
# print the JSON string representation of the object
print(TeamLineupResponse.to_json())

# convert the object into a dict
team_lineup_response_dict = team_lineup_response_instance.to_dict()
# create an instance of TeamLineupResponse from a dict
team_lineup_response_from_dict = TeamLineupResponse.from_dict(team_lineup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


