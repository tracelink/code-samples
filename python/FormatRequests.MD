# Formatting API Requests  

## HTTP Request URL

Your administrator can provide the URL you will use for submitting requests.  
These requests will use the **POST** verb.

## Request Header  

To authenticate with the APT application, include the following in the header of your HTTP request:  
A **Token** that is your authorization to make requests.  
A **Content Type** that identifies the format of the data passed.  In this case it will be *application/json*.  

## Payload  

This is the data that you will be submitting to the application to process.  In APT a request body has two distinct parts:  

### Header  

The request body header identifies how APT processes your request.  All items below are required:

| Name                 | Type    | Description                                                                                                                                           |
| -------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `headerVersion`      | integer | The version identifier for the call. Valid value is `1`.                                                                                              |
| `eventName`          | string  | The fully qualified name of the add event response. For valid values, see [event name mapping](EventNames.MD)                                         |
| `ownerID`            | string  | The identifier of the Owner company associated with the request. See [authentication](../authentication.md).                                          |
| `processNetworkId`   | string  | The network network containing the incident process. This must be a valid network in the Owner company. See [authentication](../authentication.md).   |
| `appName`            | string  | The application that owns the event. Valid value is `agile-process-teams`.                                                                            |
| `dataspace`          | string  | The dataspace inside within the environment where the request is being made. Valid value is `default`.                                                |   

### Body
A properly constructed JSON object is required as a payload. You can either dynamically create and use a JSON object at runtime or create a file with the appropriate values for importing as needed.

Each event has different parameters and requirements and is based on the value of `eventName` in the payload header. The samples folders contains payload bodies with examples containing everything required for each request event.

A simple example of a complete payload body:
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-direct-supplier-incident:v2",
        "ownerId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
        "processNetworkId": "945feb8e-09a7-4fef-9a8a-b3c5b56f87d",
        "appName": "agile-process-teams",
        "dataspace": "default"
            },
    "payload": {
        "aptBusinessObjectSummary": "Product from manufacturer does not meet specifications.",
        "directSupplierImpact": {
        "businessPriority": "HIGH"
        }
    }
}
```

# Next  
Follow [Using the API](UsingTheAPI.MD) for a walk-through.
