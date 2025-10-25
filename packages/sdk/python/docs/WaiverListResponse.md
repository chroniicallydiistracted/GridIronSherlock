# WaiverListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 
**items** | [**List[WaiverRecommendation]**](WaiverRecommendation.md) |  | 

## Example

```python
from openapi_client.models.waiver_list_response import WaiverListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WaiverListResponse from a JSON string
waiver_list_response_instance = WaiverListResponse.from_json(json)
# print the JSON string representation of the object
print(WaiverListResponse.to_json())

# convert the object into a dict
waiver_list_response_dict = waiver_list_response_instance.to_dict()
# create an instance of WaiverListResponse from a dict
waiver_list_response_from_dict = WaiverListResponse.from_dict(waiver_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


