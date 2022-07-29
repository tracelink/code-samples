# Troubleshooting error messages in the response
The Agile Process Teams (APT) API responds to each request with a status code and text describing the result of the request.  
Successful requests use a **200** status code and provide a payload.
The response payload from an unsuccessful request is null.

The application does its best to help you determine where to start when troubleshooting failed requests.  

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
        "aptBusinessObjectSummary": "Incomplete shipment received (second try).",
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
APT returns a response similar to the following:  
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
The **errMsg** item tells you the validation of the payload object failed.  In this case, the application determined the payload contains the following error: The aptBusinessObjectSummary entry is missing.  

The Direct Supplier Incident API document shows that an entry for aptBusinessObjectSummary is required.  
![API document snip](APIdocSnip.PNG)  

You update your payload to add an aptBusinessObjectSummary entry similar to this:  
```
"payload": {
	"aptBusinessObjectDescription": "Several packages missing or damaged.",
	"aptBusinessObjectSummary": "Incomplete shipment received.",
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
```
This time when you submit your request, you get a successful response.  
```
Response status code: 200
Response message {
  "header" : {
    "headerVersion" : 1,
    "eventName" : "agile-process-teams:add-direct-supplier-incident-response:v3",
    "ownerId" : "94f94f37-2772-4b39-8041-9c2dcfcfff82",
    "isErr" : false,
    "errCode" : "200_OK",
    "licensePlate" : "emPNlq-EfkPSJ"
  },
  "payload" : {
    "id" : "2846753a-65c5-4dd7-aece-1e1a00b62fa1"
  }
}
```