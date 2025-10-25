# ProjectionRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**PlayerSummary**](PlayerSummary.md) |  | 
**period** | [**ScoringPeriod**](ScoringPeriod.md) |  | 
**league_id** | **str** | Canonical UUID identifier. | [optional] 
**projection** | [**ProjectionSummary**](ProjectionSummary.md) |  | 
**opponent** | [**ProjectionRecordOpponent**](ProjectionRecordOpponent.md) |  | [optional] 
**usage** | [**ProjectionRecordUsage**](ProjectionRecordUsage.md) |  | [optional] 

## Example

```python
from openapi_client.models.projection_record import ProjectionRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectionRecord from a JSON string
projection_record_instance = ProjectionRecord.from_json(json)
# print the JSON string representation of the object
print(ProjectionRecord.to_json())

# convert the object into a dict
projection_record_dict = projection_record_instance.to_dict()
# create an instance of ProjectionRecord from a dict
projection_record_from_dict = ProjectionRecord.from_dict(projection_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


