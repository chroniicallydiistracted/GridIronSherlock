# TeamReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | 
**league_id** | **str** |  | 
**name** | **str** |  | 
**abbreviation** | **str** |  | [optional] 
**manager** | **str** |  | [optional] 
**record** | [**TeamReferenceRecord**](TeamReferenceRecord.md) |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.team_reference import TeamReference

# TODO update the JSON string below
json = "{}"
# create an instance of TeamReference from a JSON string
team_reference_instance = TeamReference.from_json(json)
# print the JSON string representation of the object
print(TeamReference.to_json())

# convert the object into a dict
team_reference_dict = team_reference_instance.to_dict()
# create an instance of TeamReference from a dict
team_reference_from_dict = TeamReference.from_dict(team_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


