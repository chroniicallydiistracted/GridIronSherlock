# gridiron_sherlock_sdk.LiveApi

All URIs are relative to *https://api.gridironsherlock.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stream_live_impacts**](LiveApi.md#stream_live_impacts) | **GET** /live/stream | Subscribe to live impact events


# **stream_live_impacts**
> LiveImpactEvent stream_live_impacts()

Subscribe to live impact events

### Example

* Api Key Authentication (sessionCookie):
* Bearer (JWT) Authentication (serviceToken):

```python
import gridiron_sherlock_sdk
from gridiron_sherlock_sdk.models.live_impact_event import LiveImpactEvent
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
    api_instance = gridiron_sherlock_sdk.LiveApi(api_client)

    try:
        # Subscribe to live impact events
        api_response = api_instance.stream_live_impacts()
        print("The response of LiveApi->stream_live_impacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveApi->stream_live_impacts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LiveImpactEvent**](LiveImpactEvent.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [serviceToken](../README.md#serviceToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server-Sent Events stream |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

