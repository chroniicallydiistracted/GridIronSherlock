# TeamReferenceRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wins** | **int** |  | 
**losses** | **int** |  | 
**ties** | **int** |  | 

## Example

```python
from openapi_client.models.team_reference_record import TeamReferenceRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TeamReferenceRecord from a JSON string
team_reference_record_instance = TeamReferenceRecord.from_json(json)
# print the JSON string representation of the object
print(TeamReferenceRecord.to_json())

# convert the object into a dict
team_reference_record_dict = team_reference_record_instance.to_dict()
# create an instance of TeamReferenceRecord from a dict
team_reference_record_from_dict = TeamReferenceRecord.from_dict(team_reference_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


