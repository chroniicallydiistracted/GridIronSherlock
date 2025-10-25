# InjuryStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**designation** | **str** |  | [optional] 
**updated_at** | **datetime** |  | 
**notes** | **str** |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.injury_status import InjuryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of InjuryStatus from a JSON string
injury_status_instance = InjuryStatus.from_json(json)
# print the JSON string representation of the object
print(InjuryStatus.to_json())

# convert the object into a dict
injury_status_dict = injury_status_instance.to_dict()
# create an instance of InjuryStatus from a dict
injury_status_from_dict = InjuryStatus.from_dict(injury_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


