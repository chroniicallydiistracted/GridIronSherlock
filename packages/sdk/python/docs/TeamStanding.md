# TeamStanding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | [**TeamReference**](TeamReference.md) |  | 
**rank** | **int** |  | 
**points_for** | **float** |  | 
**points_against** | **float** |  | 
**streak** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.team_standing import TeamStanding

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStanding from a JSON string
team_standing_instance = TeamStanding.from_json(json)
# print the JSON string representation of the object
print(TeamStanding.to_json())

# convert the object into a dict
team_standing_dict = team_standing_instance.to_dict()
# create an instance of TeamStanding from a dict
team_standing_from_dict = TeamStanding.from_dict(team_standing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


