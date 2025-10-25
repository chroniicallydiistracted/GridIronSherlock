# ProjectionRecordUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_share** | **float** |  | [optional] 
**route_share** | **float** |  | [optional] 
**target_share** | **float** |  | [optional] 
**rush_share** | **float** |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.projection_record_usage import ProjectionRecordUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectionRecordUsage from a JSON string
projection_record_usage_instance = ProjectionRecordUsage.from_json(json)
# print the JSON string representation of the object
print(ProjectionRecordUsage.to_json())

# convert the object into a dict
projection_record_usage_dict = projection_record_usage_instance.to_dict()
# create an instance of ProjectionRecordUsage from a dict
projection_record_usage_from_dict = ProjectionRecordUsage.from_dict(projection_record_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


