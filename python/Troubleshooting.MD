# Troubleshooting Errors

The APT-SCIM API responds to each request with a status code and text describing the result of the request.  

Successful requests use a **200** status code and provide a payload.

The response payload from an unsuccessful request is null.

Assume you submit the following request:  
```
{
    "header": {
        "appName": "agile-process-teams",
        "dataspace": "default",
        "eventName": "agile-process-teams:add-direct-supplier-incident:v3",
        "headerVersion": 1,
        "ownerId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
        "processNetworkId": "945feb8e-09a7-4fef-9a8a-b3c5b56f87d"
    },
    "payload": {
        "aptBusinessObjectDescription": "Several packages missing or damaged.",
        "createdByPartner": false,
        "deviationType": "UNPLANNED",
        "directSupplierImpact": {
            "businessImpact": "Business Impact",
            "businessPriority": "HIGH"
        },
        "isEscalated": false,
        "isSubmittedToPartner": false,
        "materialProblem": "SHORT_SHIPMENT_RECEIVED",
        "materialSubtype": "SHIPPED",
        "materialType": "FINISHED_GOOD",
        "resolutionDueDate": 1662012000000
    }
}
```
APT-SCIM returns a response similar to the following:  
```
comment_response = utils.post_request(reqHeader, comment_request)
Response status code: 400
Response message {
  "header" : {
    "headerVersion" : 1,
    "eventName" : "agile-process-teams:add-direct-supplier-incident-response:v3",
    "isErr" : true,
    "errCode" : "400",
    "errMsg" : "{\"validation-failed\": [\"$.aptBusinessObjectSummary: is missing but it is required\"]}",
    "licensePlate" : "GJ2jQx",
    "exceptionName" : "SchemaValidationException"
  },
  "payload" : null
}
```
The **errMsg** reveals the validation of the payload object failed.  In this case, the application determined the payload is missing `aptBusinessObjectSummary`, but it is required. 