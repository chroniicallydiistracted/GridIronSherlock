# ProjectionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 
**items** | [**List[ProjectionRecord]**](ProjectionRecord.md) |  | 

## Example

```python
from gridiron_sherlock_sdk.models.projection_list_response import ProjectionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectionListResponse from a JSON string
projection_list_response_instance = ProjectionListResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectionListResponse.to_json())

# convert the object into a dict
projection_list_response_dict = projection_list_response_instance.to_dict()
# create an instance of ProjectionListResponse from a dict
projection_list_response_from_dict = ProjectionListResponse.from_dict(projection_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


