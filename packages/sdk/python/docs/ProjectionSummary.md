# ProjectionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mean_points** | **float** |  | 
**p20** | **float** |  | 
**p50** | **float** |  | 
**p80** | **float** |  | 
**boom_probability** | **float** |  | 
**bust_probability** | **float** |  | 
**floor_points** | **float** |  | [optional] 
**ceiling_points** | **float** |  | [optional] 
**provenance** | [**Provenance**](Provenance.md) |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.projection_summary import ProjectionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectionSummary from a JSON string
projection_summary_instance = ProjectionSummary.from_json(json)
# print the JSON string representation of the object
print(ProjectionSummary.to_json())

# convert the object into a dict
projection_summary_dict = projection_summary_instance.to_dict()
# create an instance of ProjectionSummary from a dict
projection_summary_from_dict = ProjectionSummary.from_dict(projection_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


