# UserProfilePreferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_league_id** | **str** | Canonical UUID identifier. | [optional] 
**default_view** | **str** |  | [optional] 
**notification_opt_in** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.user_profile_preferences import UserProfilePreferences

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfilePreferences from a JSON string
user_profile_preferences_instance = UserProfilePreferences.from_json(json)
# print the JSON string representation of the object
print(UserProfilePreferences.to_json())

# convert the object into a dict
user_profile_preferences_dict = user_profile_preferences_instance.to_dict()
# create an instance of UserProfilePreferences from a dict
user_profile_preferences_from_dict = UserProfilePreferences.from_dict(user_profile_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


