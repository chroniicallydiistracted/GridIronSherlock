# gridiron_sherlock_sdk.PlayersApi

All URIs are relative to *https://api.gridironsherlock.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player**](PlayersApi.md#get_player) | **GET** /players/{playerId} | Get player detail
[**search_players**](PlayersApi.md#search_players) | **GET** /players | Search players


# **get_player**
> PlayerDetail get_player(player_id, league_id=league_id)

Get player detail

### Example

* Api Key Authentication (sessionCookie):
* Bearer (JWT) Authentication (serviceToken):

```python
import gridiron_sherlock_sdk
from gridiron_sherlock_sdk.models.player_detail import PlayerDetail
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
    api_instance = gridiron_sherlock_sdk.PlayersApi(api_client)
    player_id = 'player_id_example' # str | 
    league_id = 'league_id_example' # str |  (optional)

    try:
        # Get player detail
        api_response = api_instance.get_player(player_id, league_id=league_id)
        print("The response of PlayersApi->get_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**|  | 
 **league_id** | **str**|  | [optional] 

### Return type

[**PlayerDetail**](PlayerDetail.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [serviceToken](../README.md#serviceToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Player detail |  -  |
**404** | Player not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_players**
> PlayerListResponse search_players(page=page, page_size=page_size, query=query, position=position, team=team, league_id=league_id)

Search players

### Example

* Api Key Authentication (sessionCookie):
* Bearer (JWT) Authentication (serviceToken):

```python
import gridiron_sherlock_sdk
from gridiron_sherlock_sdk.models.player_list_response import PlayerListResponse
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
    api_instance = gridiron_sherlock_sdk.PlayersApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 25 # int |  (optional) (default to 25)
    query = 'query_example' # str |  (optional)
    position = 'position_example' # str |  (optional)
    team = 'team_example' # str |  (optional)
    league_id = 'league_id_example' # str |  (optional)

    try:
        # Search players
        api_response = api_instance.search_players(page=page, page_size=page_size, query=query, position=position, team=team, league_id=league_id)
        print("The response of PlayersApi->search_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->search_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 25]
 **query** | **str**|  | [optional] 
 **position** | **str**|  | [optional] 
 **team** | **str**|  | [optional] 
 **league_id** | **str**|  | [optional] 

### Return type

[**PlayerListResponse**](PlayerListResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [serviceToken](../README.md#serviceToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated player summaries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

