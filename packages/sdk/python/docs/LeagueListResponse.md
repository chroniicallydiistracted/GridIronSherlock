# LeagueListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 
**items** | [**List[LeagueSummary]**](LeagueSummary.md) |  | 

## Example

```python
from gridiron_sherlock_sdk.models.league_list_response import LeagueListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueListResponse from a JSON string
league_list_response_instance = LeagueListResponse.from_json(json)
# print the JSON string representation of the object
print(LeagueListResponse.to_json())

# convert the object into a dict
league_list_response_dict = league_list_response_instance.to_dict()
# create an instance of LeagueListResponse from a dict
league_list_response_from_dict = LeagueListResponse.from_dict(league_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


