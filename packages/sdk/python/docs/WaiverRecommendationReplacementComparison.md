# WaiverRecommendationReplacementComparison


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop_player_id** | **str** | Canonical UUID identifier. | [optional] 
**delta_points** | **float** |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.waiver_recommendation_replacement_comparison import WaiverRecommendationReplacementComparison

# TODO update the JSON string below
json = "{}"
# create an instance of WaiverRecommendationReplacementComparison from a JSON string
waiver_recommendation_replacement_comparison_instance = WaiverRecommendationReplacementComparison.from_json(json)
# print the JSON string representation of the object
print(WaiverRecommendationReplacementComparison.to_json())

# convert the object into a dict
waiver_recommendation_replacement_comparison_dict = waiver_recommendation_replacement_comparison_instance.to_dict()
# create an instance of WaiverRecommendationReplacementComparison from a dict
waiver_recommendation_replacement_comparison_from_dict = WaiverRecommendationReplacementComparison.from_dict(waiver_recommendation_replacement_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


