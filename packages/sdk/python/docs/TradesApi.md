# openapi_client.TradesApi

All URIs are relative to *https://api.gridironsherlock.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**estimate_trade**](TradesApi.md#estimate_trade) | **POST** /trades/estimate | Estimate trade fairness and impact


# **estimate_trade**
> TradeEstimateResponse estimate_trade(trade_estimate_request)

Estimate trade fairness and impact

### Example

* Api Key Authentication (sessionCookie):
* Bearer (JWT) Authentication (serviceToken):

```python
import openapi_client
from openapi_client.models.trade_estimate_request import TradeEstimateRequest
from openapi_client.models.trade_estimate_response import TradeEstimateResponse
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
    api_instance = openapi_client.TradesApi(api_client)
    trade_estimate_request = openapi_client.TradeEstimateRequest() # TradeEstimateRequest | 

    try:
        # Estimate trade fairness and impact
        api_response = api_instance.estimate_trade(trade_estimate_request)
        print("The response of TradesApi->estimate_trade:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradesApi->estimate_trade: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trade_estimate_request** | [**TradeEstimateRequest**](TradeEstimateRequest.md)|  | 

### Return type

[**TradeEstimateResponse**](TradeEstimateResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [serviceToken](../README.md#serviceToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Trade impact estimate |  -  |
**400** | Invalid trade payload |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

