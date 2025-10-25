# ProjectionRecordOpponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | [optional] 
**home** | **bool** |  | [optional] 
**implied_total** | **float** |  | [optional] 
**pace_rank** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.projection_record_opponent import ProjectionRecordOpponent

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectionRecordOpponent from a JSON string
projection_record_opponent_instance = ProjectionRecordOpponent.from_json(json)
# print the JSON string representation of the object
print(ProjectionRecordOpponent.to_json())

# convert the object into a dict
projection_record_opponent_dict = projection_record_opponent_instance.to_dict()
# create an instance of ProjectionRecordOpponent from a dict
projection_record_opponent_from_dict = ProjectionRecordOpponent.from_dict(projection_record_opponent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


