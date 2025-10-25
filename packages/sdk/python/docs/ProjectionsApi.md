# gridiron_sherlock_sdk.ProjectionsApi

All URIs are relative to *https://api.gridironsherlock.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_projections**](ProjectionsApi.md#list_projections) | **GET** /projections | List player projections


# **list_projections**
> ProjectionListResponse list_projections(page=page, page_size=page_size, season=season, week=week, position=position, league_id=league_id)

List player projections

### Example

* Api Key Authentication (sessionCookie):
* Bearer (JWT) Authentication (serviceToken):

```python
import gridiron_sherlock_sdk
from gridiron_sherlock_sdk.models.projection_list_response import ProjectionListResponse
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
    api_instance = gridiron_sherlock_sdk.ProjectionsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 25 # int |  (optional) (default to 25)
    season = 56 # int |  (optional)
    week = 56 # int |  (optional)
    position = 'position_example' # str |  (optional)
    league_id = 'league_id_example' # str |  (optional)

    try:
        # List player projections
        api_response = api_instance.list_projections(page=page, page_size=page_size, season=season, week=week, position=position, league_id=league_id)
        print("The response of ProjectionsApi->list_projections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectionsApi->list_projections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 25]
 **season** | **int**|  | [optional] 
 **week** | **int**|  | [optional] 
 **position** | **str**|  | [optional] 
 **league_id** | **str**|  | [optional] 

### Return type

[**ProjectionListResponse**](ProjectionListResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [serviceToken](../README.md#serviceToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated projections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

