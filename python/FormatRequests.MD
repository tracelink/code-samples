# Formatting API Requests  

## HTTP Request  

### Request URL  

Your administrator can provide the URL you will use for submitting requests.  
These requests will use the **POST** verb.

### Request Headers  

To authenticate with the APT application, include the following in the header of your HTTP request:  
A **Token** that is your authorization to make requests.  
A **Content Type** that identifies the format of the data passed.  In this case it will be *application/json*.  

### Request Body  

This is the data that you will be submitting to the application to process.  In APT a request body has two distinct parts:  

#### Header  

This is not to be confused with HTTP headers.  The request body header identifies how APT will process your request.  These items include:  
- **headerVersion:** Integer, **Required**.The version identifier for the call. Valid value is 1.  
- **eventName:** String, **Required**.The fully qualified name of the add event response.  *This value will change depending on the event requested*.  
- **ownerId:** String, **Required**. The identifier for the Owner company associated with the request.  
- **processNetworkId:** String, **Required**. The network that contains the incident process. This must be a valid network at the Owner company.  
- **appName:** String, **Required**. The application that owns the event. Valid value is *agile-process-teams*.  
- **dataspace:** String, **Required**. The dataspace within the environment where the request is being made. Valid value for the Production and Validation environments is **default**.    

#### Payload
The payload is the request body.  Each event will have different parameters and requirements.  A properly constructed JavaScript Object Notation (JSON) object is required as a payload.  The samples folders contain the payload bodies with examples of all the data required for each request event.  You need to provide the corresponding data for your own environment for them to work properly.

*You can either dynamically create and use a JSON object at runtime or create a file with the appropriate values for importing as needed.*  

A simple example of a complete request is as follows:  
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-direct-supplier-incident:v2",
        "ownerId": owner.get('ownerId'),
        "processNetworkId": owner.get('processNetworkId'),
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
Determine the correct **eventName** to use in your header using the [Event name mapping](EventNames.MD) guide.  
Refer to the [Using the API readme](UsingTheAPI.MD) for a walk-through.  
