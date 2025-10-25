# gridiron_sherlock_sdk.RefreshApi

All URIs are relative to *https://api.gridironsherlock.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trigger_refresh**](RefreshApi.md#trigger_refresh) | **POST** /refresh/{scope} | Trigger a background refresh


# **trigger_refresh**
> RefreshResponse trigger_refresh(scope, refresh_request=refresh_request)

Trigger a background refresh

### Example

* Api Key Authentication (sessionCookie):
* Bearer (JWT) Authentication (serviceToken):

```python
import gridiron_sherlock_sdk
from gridiron_sherlock_sdk.models.refresh_request import RefreshRequest
from gridiron_sherlock_sdk.models.refresh_response import RefreshResponse
from gridiron_sherlock_sdk.models.scope_id import ScopeId
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
    api_instance = gridiron_sherlock_sdk.RefreshApi(api_client)
    scope = gridiron_sherlock_sdk.ScopeId() # ScopeId | 
    refresh_request = gridiron_sherlock_sdk.RefreshRequest() # RefreshRequest |  (optional)

    try:
        # Trigger a background refresh
        api_response = api_instance.trigger_refresh(scope, refresh_request=refresh_request)
        print("The response of RefreshApi->trigger_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefreshApi->trigger_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | [**ScopeId**](.md)|  | 
 **refresh_request** | [**RefreshRequest**](RefreshRequest.md)|  | [optional] 

### Return type

[**RefreshResponse**](RefreshResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [serviceToken](../README.md#serviceToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Refresh enqueued |  -  |
**400** | Invalid refresh request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

