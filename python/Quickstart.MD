# APT-SCWM API Quickstart

This quickstart covers:

1. Creating a direct supplier incident using the APT-SCWM API
2. Using the response data to add a comment to the created incident   

*This example uses Python version 3.10 or later entering commands in a Python terminal.*  

To follow along with the example, open your preferred Python terminal and use a single session through the entire process.  

## Create Your Request  


### Request Body  

For this example, we create the request body first.  In its simplest form, the request body contains a header and a payload and conforms to this format:
```
{
  "header":{},
  "payload":{}
}
```
**Type or copy the following into your Python terminal**  
```
request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:add-direct-supplier-incident:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
    },
  "payload": {
    "aptBusinessObjectSummary": "Incomplete shipment received.",
    "aptBusinessObjectDescription": "Several packages missing or damaged.",
    "deviationType": "UNPLANNED",
    "materialType": "FINISHED_GOOD",
    "materialSubtype": "SHIPPED",
    "materialProblem": "SHORT_SHIPMENT_RECEIVED",
    "isEscalated": False,
    "createdByPartner": False,
    "isSubmittedToPartner": False,
    "directSupplierImpact": {
      "businessImpact": "Business Impact",
      "businessPriority": "HIGH"
    }
  }
}
```
This creates a dictionary object containing the `header` and `payload` elements we discussed earlier.  You can work through the items in this dictionary using standard Python methods.  This allows you to make any desired modifications prior to packaging and submitting your request.  

As an example, let's change the priority of this incident from `HIGH` to `MEDIUM`.  To change this value, we must reference the `businessPriority` item.  To reach this value, reference the `directSupplierImpact` element of the `payload`.  
**Type or copy the following into your Python terminal**
```
request_body.get('payload').get('directSupplierImpact').update({'businessPriority': 'MEDIUM'})
```
We use the `.get()` method for each element in our tree that we wish to access.  The `.update()` method allows us to change a value by referencing its key.
Use care to include the braces `{}` when updating an item.

### Request Header
APT-SCWM uses tokens for authentication.  For single interactive requests, you can use a bearer token (a token that usually expires within an hour) or a longer-lived token for automated processes.  The token is a string that contains 'user:password' in Base64 encoding.

**Type or copy the following into your Python terminal**  
```
method = 'Basic'
token = 'YOUR_TOKEN_HERE'
request_headers = {"Authorization": "{0} {1}".format(method, token), "Content-Type": "application/json"}
```
The resulting headers variable will look similar to  
`{'Authorization': 'Basic YOUR_TOKEN_HERE', 'Content-Type': 'application/json'}`  

You are free to use any method you wish to create the request header.  APT-SCWM requires at a minimum an `Authorization` item containing a method and a token along with a `Content-Type` of `application/json`.

## Package Your Request  
At this point you have a request body and a request header.  You have made all required modifications using the Python dictionary methods.  APT-SCWM requires requests formatted as JSON (JavaScript Object Notation).  

Until now, we have been using a Python terminal without any additional packages.  It's time to add the JSON library so we can translate our dictionary into a format accepted by APT-SCWM.  The JSON library is included in the Python installation by default, so no extra installations are required.  

You may wish to verify your request prior to submission.  The `json.dumps()`` method of the json library can help.  Use this method against your existing `request_body` dictionary to see what the `json.dumps()` method will generate.  

**Type or copy the following into your Python terminal**  
`print(json.dumps(request_body, indent=4, sort_keys=False))`
The response is similar to:  
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-direct-supplier-incident:v3",
        "ownerId": "YOUR_OWNER_ID",
        "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
        "appName": "agile-process-teams",
        "dataspace": "default"
    },
    "payload": {
        "aptBusinessObjectSummary": "Incomplete shipment received.",
        "aptBusinessObjectDescription": "Several packages missing or damaged.",
        "deviationType": "UNPLANNED",
        "materialType": "FINISHED_GOOD",
        "materialSubtype": "SHIPPED",
        "materialProblem": "SHORT_SHIPMENT_RECEIVED",
        "isEscalated": false,
        "createdByPartner": false,
        "isSubmittedToPartner": false,
        "directSupplierImpact": {
            "businessImpact": "Business Impact",
            "businessPriority": "MEDIUM"
        }
    }
}
```  
Note that your `False` values have been converted to `false` according to the JSON specification.  Everything looks good, so we can convert our dictionary to a JSON string.  

**Type or copy the following into your Python terminal**  
```
import json
request_body_json = json.dumps(request_body)
```

## Send Request
Once your request header and request body are complete you are ready to submit your request.  
You will need the URL for the APT-SCWM environment.  Contact your administrator for this information.  
APT-SCWM uses and event driven API that communicates using the POST verb of the request/response model.  Create a variable to hold the response so you can work with your results.
**Type or copy the following into your Python terminal**  
```
url = "URL_FROM_YOUR_ADMINISTRATOR"
response = requests.request("POST", url, headers=request_header, data=request_body)
```
An example successful response:
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-direct-supplier-incident-response:v3",
        "ownerId": "YOUR_OWNER_ID",
        "isErr": false,
        "errCode": "200_OK",
        "licensePlate": "LICENSE_PLATE_ID"
    },
    "payload": {
        "id": "ITEM_ID"
    }
}
```

## Response Handling

The `id` in a successful response payload is the identifier of the created incident. Notice that the response is a string, not a JSON object. To get this identifier, enter the following in your Python terminal:
```
import json
response_json = json.loads(result.text)
incident_id = response_json.get('payload').get('id')
```

To ensure your value stored properly, enter the following in your Python terminal:
```
incident_id
'ITEM_ID'
```

## Add Incident Comment

Prepare a comment payload file called `comment_payload.json` containing the below:
```
{
	"payload": {
		"processId": "ITEM_ID",
		"processType": "directSupplierIncident",
		"aptCommentBox":{
			"aptComment":{
				"commentText": "Please provide a list of missing items and we will replace them.",
				"visibilityType": "Public"
				}
			}
		}
}
```

Do not worry that your `processId` does not match the example. You can load the payload comment file and update the `processId` number dynamically. Enter the following in your Python terminal:
```
comment_payload_file = 'comment_payload.json'
comment_payload = utils.read_payload_file(comment_payload_file)
comment_payload
{'processId': 'ITEM_ID', 'processType': 'directSupplierIncident', 'aptCommentBox': {'aptComment': {'commentText': 'Please provide a list of missing items and we will replace them.', 'visibilityType': 'Public'}}}
```
Your payload has been loaded properly, but the `processId` is still wrong. Use the `update()` function to change the stored value:
```
comment_payload.update({"processId": "ITEM_ID"})
comment_payload
{'processId': 'ITEM_ID', 'processType': 'directSupplierIncident', 'aptCommentBox': {'aptComment': {'commentText': 'Please provide a list of missing items and we will replace them.', 'visibilityType': 'Public'}}}
```
You can use the same process to change the `eventName`:
```
event_data.update({"eventName": "agile-process-teams:add-comment-for-incident:v1"})
event_data
{'eventName': 'agile-process-teams:add-comment-for-incident:v1', 'ownerId': '2aaeed40-3912-427e-a94f-51fd5a730345', 'processNetworkId': '61077cb2-601b-4c27-b11f-5e3910589931'}
```
The payload and event data should now be updated. You can verify this by resending the commands to build the request body and resend the request.  
```
request_body = utils.create_payload(event_data, payload_data)
comment_result = utils.post_reqeust(request_headers, requst_body)
```
The response:  
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-comment-for-incident-response:v1",
        "ownerId": "YOUR_OWNER_ID",
        "isErr": false,
        "errCode": "200_OK",
        "licensePlate": "vXPsFz"
    },
    "payload": {
        "id": "COMMENT_ID"
    }
}
```
## Read the details of your newly created incident
In a previous step, you stored your incident id as a variable in your session.  You can use this stored variable to retrieve details about the incident.  
Use the same methods outlined above to generate a request similar to the following:
```
{
   "header": {
       "headerVersion": 1,
       "eventName": "agile-process-teams:read-directSupplierIncident:v3",
       "ownerId": "YOUR_OWNER_ID",
       "appName": "agile-process-teams",
       "dataspace": "default",
       "processNetworkId": "YOUR_PROCESS_NETWORK_ID"
   },
   "payload": {
       "id": "ITEM_ID"
   }
}
```
The response provides the complete record for the incident:
```
{
"header": {
	"headerVersion": 1,
	"eventName": "agile-process-teams:read-directSupplierIncident-response:v3",
	"ownerId": "YOUR_OWNER_ID",
	"isErr": false,
	"errCode": "200_OK",
	"licensePlate": "Y7yRFr-tRpXpc"
},
"payload": {
	"createdByUserId": "YOUR_OWNER_ID",
	"schemaVersion": 3,
	"data": {
		"aptBusinessObjectSummary": "Kinaxis - Late: PO, Exception ID: 37495023853_jlocky",
		"aptBusinessObjectDescription": "Order:PO_B2710_S006_2101130836, Line:4, Type:PO",
		"responsibleDepartmentAtPartner": "CONTRACT_MANAGEMENT",
		"responsibleDepartmentAtCompany": "SUPPLY_CHAIN",
		"businessPriority": "HIGH",
		"incidentType": "MATERIAL_SHORTAGE",
		"otherIncidentType": "Purchase Order Discrepancy",
		"aptBusinessObjectImpactsLocationMasterData": [],
		"currentlyAssignedPartnerUsersId": [
			"YOUR_OWNER_ID"
		],
		"resolutionDueDate": 1661817600000,
		"referenceIdentifiers": [
			{
				"referenceTransactionType": "PO_NUMBER",
				"value": " Order:PO_B2710_S006_2101130836, Line:4, Type:PO"
			}
		],
		"response": {},
		"responsiblePartyAtPartnerUserId": "b2491d20-0f8b-41f5-b7aa-a4e4a04afbce",
		"responsiblePartyAtCompanyUserId": "b2491d20-0f8b-41f5-b7aa-a4e4a04afbce",
		"currentlyAssignedCompanyUsersId": [
			"b2491d20-0f8b-41f5-b7aa-a4e4a04afbce"
		],
		"primaryPartnerLocationId": "2e485684-fdd7-4ad1-8735-af4deed325f0",
		"fkProcessNetworkId": "YOUR_PROCESS_NETWORK_ID",
		"aptBusinessObjectId": "USPT-1151",
		"aptBusinessObjectIntegerIdentifier": 1151,
		"createdByPartner": false,
		"aptBusinessObjectAssignedToCompanyPartnerMasterData": {
			"partnerId": "b2491d20-0f8b-41f5-b7aa-a4e4a04afbce",
			"toIdType": "partnerMasterData"
		},
		"followerId": [
			"b2491d20-0f8b-41f5-b7aa-a4e4a04afbce"
		],
		"aptBusinessObjectNumericIdentifierDerivedField": "1151",
		"businessPriorityDerivedField": "c",
		"incidentConclusion": {
			"resolutionType": "NOT_AN_ISSUE",
			"isReoccuring": true,
			"dateClosed": 1661528887906,
			"finalRootCause": "OTHER"
		},
		"advanceMetrics": {
			"timeToClose": 3,
			"closedOnTime": true
		}
	},
	"dataVersion": 2,
	"ownerId": "YOUR_OWNER_ID",
	"objectType": "agile-process-teams:directSupplierIncident",
	"currentBaseState": "Closed",
	"schemaId": "agile-process-teams:directSupplierIncident",
	"lastUpdatedByUserId": "YOUR_OWNER_ID",
	"contextualOwnerId": "YOUR_OWNER_ID",
	"id": "ITEM_ID",
	"lastUpdatedDateTime": 1661528888803,
	"creationDateTime": 1661276934457
}
}
```
# Parked Text  
Use the following command to import the JSON and Requests libraries  
**type or copy the following into a Python terminal:**
```import json, requests```  


## Next steps
You will need a mechanism to create or update your payload data whether it is stored in a file or submitted at runtime and discarded.  
You will also need a method to maintain or refer to the `processId` number of each incident.  

## Troubleshooting
Review the [troubleshooting primer](Troubleshooting.MD).
