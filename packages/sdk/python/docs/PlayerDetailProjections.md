# PlayerDetailProjections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weekly** | [**ProjectionSummary**](ProjectionSummary.md) |  | 
**ros** | [**ProjectionSummary**](ProjectionSummary.md) |  | [optional] 

## Example

```python
from openapi_client.models.player_detail_projections import PlayerDetailProjections

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerDetailProjections from a JSON string
player_detail_projections_instance = PlayerDetailProjections.from_json(json)
# print the JSON string representation of the object
print(PlayerDetailProjections.to_json())

# convert the object into a dict
player_detail_projections_dict = player_detail_projections_instance.to_dict()
# create an instance of PlayerDetailProjections from a dict
player_detail_projections_from_dict = PlayerDetailProjections.from_dict(player_detail_projections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


