# Provenance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Data source or model name. | 
**as_of** | **datetime** | Timestamp the data was computed. | 
**model_version** | **str** | Optional model or dataset version. | [optional] 
**notes** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.provenance import Provenance

# TODO update the JSON string below
json = "{}"
# create an instance of Provenance from a JSON string
provenance_instance = Provenance.from_json(json)
# print the JSON string representation of the object
print(Provenance.to_json())

# convert the object into a dict
provenance_dict = provenance_instance.to_dict()
# create an instance of Provenance from a dict
provenance_from_dict = Provenance.from_dict(provenance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


