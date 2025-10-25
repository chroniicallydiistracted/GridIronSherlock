# openapi_client.AccountApi

All URIs are relative to *https://api.gridironsherlock.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_user**](AccountApi.md#get_current_user) | **GET** /me | Get the authenticated user profile
[**handle_o_auth_callback**](AccountApi.md#handle_o_auth_callback) | **GET** /oauth/{provider}/callback | Handle OAuth callback response
[**start_account_link**](AccountApi.md#start_account_link) | **POST** /accounts/{provider}/link | Begin OAuth linking for a provider


# **get_current_user**
> UserProfile get_current_user()

Get the authenticated user profile

### Example

* Api Key Authentication (sessionCookie):
* Bearer (JWT) Authentication (serviceToken):

```python
import openapi_client
from openapi_client.models.user_profile import UserProfile
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
    api_instance = openapi_client.AccountApi(api_client)

    try:
        # Get the authenticated user profile
        api_response = api_instance.get_current_user()
        print("The response of AccountApi->get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_current_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [serviceToken](../README.md#serviceToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authenticated user profile |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_o_auth_callback**
> OAuthCallbackResponse handle_o_auth_callback(provider, code=code, state=state)

Handle OAuth callback response

### Example

* Api Key Authentication (sessionCookie):
* Bearer (JWT) Authentication (serviceToken):

```python
import openapi_client
from openapi_client.models.o_auth_callback_response import OAuthCallbackResponse
from openapi_client.models.provider_id import ProviderId
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
    api_instance = openapi_client.AccountApi(api_client)
    provider = openapi_client.ProviderId() # ProviderId | 
    code = 'code_example' # str | Authorization code returned by the provider. (optional)
    state = 'state_example' # str | Opaque state parameter for CSRF protection. (optional)

    try:
        # Handle OAuth callback response
        api_response = api_instance.handle_o_auth_callback(provider, code=code, state=state)
        print("The response of AccountApi->handle_o_auth_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->handle_o_auth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**ProviderId**](.md)|  | 
 **code** | **str**| Authorization code returned by the provider. | [optional] 
 **state** | **str**| Opaque state parameter for CSRF protection. | [optional] 

### Return type

[**OAuthCallbackResponse**](OAuthCallbackResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [serviceToken](../README.md#serviceToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Callback processed |  -  |
**400** | Callback validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_account_link**
> AccountLinkResponse start_account_link(provider, account_link_request=account_link_request)

Begin OAuth linking for a provider

### Example

* Api Key Authentication (sessionCookie):
* Bearer (JWT) Authentication (serviceToken):

```python
import openapi_client
from openapi_client.models.account_link_request import AccountLinkRequest
from openapi_client.models.account_link_response import AccountLinkResponse
from openapi_client.models.provider_id import ProviderId
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
    api_instance = openapi_client.AccountApi(api_client)
    provider = openapi_client.ProviderId() # ProviderId | 
    account_link_request = openapi_client.AccountLinkRequest() # AccountLinkRequest |  (optional)

    try:
        # Begin OAuth linking for a provider
        api_response = api_instance.start_account_link(provider, account_link_request=account_link_request)
        print("The response of AccountApi->start_account_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->start_account_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**ProviderId**](.md)|  | 
 **account_link_request** | [**AccountLinkRequest**](AccountLinkRequest.md)|  | [optional] 

### Return type

[**AccountLinkResponse**](AccountLinkResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [serviceToken](../README.md#serviceToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OAuth redirect instructions |  -  |
**400** | Invalid request |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

