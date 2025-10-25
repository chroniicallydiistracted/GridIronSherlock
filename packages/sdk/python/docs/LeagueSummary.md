# LeagueSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league_id** | **str** | Canonical UUID identifier. | 
**provider** | [**ProviderId**](ProviderId.md) |  | 
**name** | **str** |  | 
**season** | **int** |  | 
**format** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**last_sync_at** | **datetime** |  | [optional] 
**teams** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.league_summary import LeagueSummary

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueSummary from a JSON string
league_summary_instance = LeagueSummary.from_json(json)
# print the JSON string representation of the object
print(LeagueSummary.to_json())

# convert the object into a dict
league_summary_dict = league_summary_instance.to_dict()
# create an instance of LeagueSummary from a dict
league_summary_from_dict = LeagueSummary.from_dict(league_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


