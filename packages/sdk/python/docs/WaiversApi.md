# openapi_client.WaiversApi

All URIs are relative to *https://api.gridironsherlock.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_waivers**](WaiversApi.md#list_waivers) | **GET** /waivers | List waiver recommendations


# **list_waivers**
> WaiverListResponse list_waivers(league_id, week=week, season=season)

List waiver recommendations

### Example

* Api Key Authentication (sessionCookie):
* Bearer (JWT) Authentication (serviceToken):

```python
import openapi_client
from openapi_client.models.waiver_list_response import WaiverListResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gridironsherlock.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WaiversApi(api_client)
    league_id = 'league_id_example' # str | 
    week = 56 # int |  (optional)
    season = 56 # int |  (optional)

    try:
        # List waiver recommendations
        api_response = api_instance.list_waivers(league_id, week=week, season=season)
        print("The response of WaiversApi->list_waivers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaiversApi->list_waivers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **str**|  | 
 **week** | **int**|  | [optional] 
 **season** | **int**|  | [optional] 

### Return type

[**WaiverListResponse**](WaiverListResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [serviceToken](../README.md#serviceToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated waiver recommendations |  -  |
**400** | Missing required league |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

