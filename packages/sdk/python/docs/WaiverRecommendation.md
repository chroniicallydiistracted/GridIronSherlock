# WaiverRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**PlayerSummary**](PlayerSummary.md) |  | 
**projected_points** | **float** |  | 
**faab** | [**FAABRange**](FAABRange.md) |  | 
**priority** | **int** |  | 
**recommended_action** | **str** |  | 
**reason** | **str** |  | [optional] 
**replacement_comparison** | [**WaiverRecommendationReplacementComparison**](WaiverRecommendationReplacementComparison.md) |  | [optional] 
**provenance** | [**Provenance**](Provenance.md) |  | [optional] 

## Example

```python
from gridiron_sherlock_sdk.models.waiver_recommendation import WaiverRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of WaiverRecommendation from a JSON string
waiver_recommendation_instance = WaiverRecommendation.from_json(json)
# print the JSON string representation of the object
print(WaiverRecommendation.to_json())

# convert the object into a dict
waiver_recommendation_dict = waiver_recommendation_instance.to_dict()
# create an instance of WaiverRecommendation from a dict
waiver_recommendation_from_dict = WaiverRecommendation.from_dict(waiver_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


