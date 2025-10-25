# gridiron_sherlock_sdk.TeamsApi

All URIs are relative to *https://api.gridironsherlock.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_team_lineup**](TeamsApi.md#get_team_lineup) | **GET** /teams/{teamId}/lineup | Get the tracked lineup for a team
[**optimize_team_lineup**](TeamsApi.md#optimize_team_lineup) | **POST** /teams/{teamId}/optimize | Run the lineup optimizer


# **get_team_lineup**
> TeamLineupResponse get_team_lineup(team_id, season=season, week=week)

Get the tracked lineup for a team

### Example

* Api Key Authentication (sessionCookie):
* Bearer (JWT) Authentication (serviceToken):

```python
import gridiron_sherlock_sdk
from gridiron_sherlock_sdk.models.team_lineup_response import TeamLineupResponse
from gridiron_sherlock_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gridironsherlock.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gridiron_sherlock_sdk.Configuration(
    host = "https://api.gridironsherlock.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionCookie
configuration.api_key['sessionCookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionCookie'] = 'Bearer'

# Configure Bearer authorization (JWT): serviceToken
configuration = gridiron_sherlock_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gridiron_sherlock_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridiron_sherlock_sdk.TeamsApi(api_client)
    team_id = 'team_id_example' # str | 
    season = 56 # int |  (optional)
    week = 56 # int |  (optional)

    try:
        # Get the tracked lineup for a team
        api_response = api_instance.get_team_lineup(team_id, season=season, week=week)
        print("The response of TeamsApi->get_team_lineup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team_lineup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **season** | **int**|  | [optional] 
 **week** | **int**|  | [optional] 

### Return type

[**TeamLineupResponse**](TeamLineupResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [serviceToken](../README.md#serviceToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team lineup snapshot |  -  |
**404** | Team not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **optimize_team_lineup**
> OptimizationResponse optimize_team_lineup(team_id, optimization_request)

Run the lineup optimizer

### Example

* Api Key Authentication (sessionCookie):
* Bearer (JWT) Authentication (serviceToken):

```python
import gridiron_sherlock_sdk
from gridiron_sherlock_sdk.models.optimization_request import OptimizationRequest
from gridiron_sherlock_sdk.models.optimization_response import OptimizationResponse
from gridiron_sherlock_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gridironsherlock.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gridiron_sherlock_sdk.Configuration(
    host = "https://api.gridironsherlock.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionCookie
configuration.api_key['sessionCookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionCookie'] = 'Bearer'

# Configure Bearer authorization (JWT): serviceToken
configuration = gridiron_sherlock_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gridiron_sherlock_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridiron_sherlock_sdk.TeamsApi(api_client)
    team_id = 'team_id_example' # str | 
    optimization_request = gridiron_sherlock_sdk.OptimizationRequest() # OptimizationRequest | 

    try:
        # Run the lineup optimizer
        api_response = api_instance.optimize_team_lineup(team_id, optimization_request)
        print("The response of TeamsApi->optimize_team_lineup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->optimize_team_lineup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **optimization_request** | [**OptimizationRequest**](OptimizationRequest.md)|  | 

### Return type

[**OptimizationResponse**](OptimizationResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [serviceToken](../README.md#serviceToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Optimization result |  -  |
**400** | Invalid optimization request |  -  |
**409** | Optimization could not converge |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

