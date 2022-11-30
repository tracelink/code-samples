# APT-SCWM API Quickstart

This quickstart covers:

1. Creating a direct supplier incident using the APT-SCWM API
2. Using the response data to add a comment to the created incident   

*This example uses Python version 3.10 or later entering commands in a Python terminal.*  

## Request Body

Use the following command to import the JSON and Requests libraries  
```import json, requests```  

For this example, we are working backwards from the request body. In its simplest form, the request body contains a header and a payload.  A request body resembles the following:
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-direct-supplier-incident:v2",
        "ownerId": "YOUR_OWNER_ID",
        "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
        "appName": "agile-process-teams",
        "dataspace": "default"
    },
    "payload": {
        "aptBusinessObjectSummary": "Raw materials shortage at Location XYZ",
        "directSupplierImpact": {
            "businessPriority": "MEDIUM"
        }
    }
}
```

Many requests share common values in the header. The `headerVersion`, `appName`, and `dataspace` do not change often. For a single company, the `ownerId` and `processNetworkId` values are likely to remain the same. This means you may only need to determine the `eventName` for the request you submit. The payload will change with each new request depending on the selected `eventName`. As the integrator, you can store these values after creation or generate and use them dynamically at runtime.  

### Create a Payload

The APT-SCWM API uses JSON for passing data. The minimum required data to submit a direct supplier incident is a summary of the incident and an impact priority level.  Below is a basic example of the minimum required payload:
```
{
"payload": {
    "aptBusinessObjectSummary": "Automation test from samples folder.",
     "directSupplierImpact": {
        "businessPriority": "LOW"
        }
    }
}
```

We can store payloads in text files and read them into our Python session as we need them. You may use any text editor capable of specifying the JSON file type to create a file containing your payload data.  

We can also dynamically create and modify payloads as needed during a session.  

For this example, type or copy the following into a Python terminal:  
```
my_payload = {
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
This creates a dictionary object.  You can verify this in your terminal by entering the command `type(my_payload)`.  The response should be `<class 'dict'>`.

You can use the `.get('item')` method to refer to the individual elements inside the payload.  For example, if you enter `my_payload.get('payload')`, you will get the above with the "payload" section omitted.  It's not really omitted, you are seeing inside the payload element.  
You can continue navigating the payload object by referencing further items.  Try entering the following: `my_payload.get('payload').get('isEscalated')`.  Your response should look something like this:  
`False`  

Take care when using boolean values.  Python represents them as `True` or `False`.  By contrast, JSON uses `true` and `false`.  This seemingly insignificant difference can cause difficulties when working in a terminal session.  

Before we submit our request, we must format our data as a JSON object.

In your Python terminal, enter the following:  
```
my_file = 'addIncident.json'  # include full path if needed
with open(my_file, 'r') as file_in:
  data = file_in.read()
json_object = json.loads(data)

If you want to keep the 'payload' identifier in your string, omit this step
my_payload = j_object.get("payload")
payload_data = utils.read_payload_file(my_file)
```  
If you already use a JSON payload as part of your other processes, you can use the `accept_json_payload(payload_in)` function instead. This function accepts a JSON object, checks for proper format, and does some minor processing for insertion into the request body.

In the Python terminal, enter the following:
```
my_json_data = result_from_some_other_process()
payload_data = utils.accept_json_payload(my_json_data)
```

### Header

Now that you have usable payload data, you need to inform APT how to process the payload.  

In your Python terminal, enter the following, replacing values with your own:
```
event_data = {"eventName": "agile-process-teams:add-direct-supplier-incident:v2",
                  "ownerId": "REPLACE_WITH_YOURS",
                  "processNetworkId": "REPLACE_WITH_YOURS"}
```
This dictionary is passed in as a parameter to the `utils.create_payload(event_in, payload_in)` function.  This function places the header and payload JSON items properly in the request body.  

Please note there is no error handling logic in these samples, you need to create your own.

Now, create the full request body. In your Python terminal, enter the following:
```
request_body = utils.create_payload(event_data, payload_data)
```

## Request Header

The `utils.py` file provides a function to create a request header that can be reused until token expiration.  

In your Python terminal, enter the following:  
```
my_token = however_you_get_your_token()
my_header = utils.create_headers(my_token)
my_header
{'Authorization': 'Bearer tokenhere', 'Content-Type': 'application/json'}
```

## Preview Request

If you wish to check your request prior to sending it, the `utils.py` file has a mock request function that will print your payload in formatted JSON, making it easier to check against the API documentation.

In your Python terminal, enter the following:  
```
utils.mock_request(request_header, request_body)
HTML request header:
{'Authorization': 'Bearer my_token', 'Content-Type': 'application/json'}
Body of event request:
{
    "header": {
        "appName": "agile-process-teams",
        "dataspace": "default",
        "eventName": "agile-process-teams:add-direct-supplier-incident:v2",
        "headerVersion": 1,
        "ownerId": "YOUR_OWNER_ID",
        "processNetworkId": "YOUR_PROCESS_NETWORK_ID"
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
            "businessPriority": "HIGH"
            }
        }
}
```

## Send Request

Once you have a request header, body header, and body payload you are ready to submit your request.

The `utils.py` file contains a function to send your request and capture the response.

An example Python terminal session:
```
import utils
my_file = 'addIncident.json'
my_token = token_received_from_other_processes

event_data = {"eventName": "agile-process-teams:add-direct-supplier-incident:v2",
                  "ownerId": "YOUR_OWNER_ID",
                  "processNetworkId": "YOUR_PROCESS_NETWORK_ID"}
request_headers = utils.create_headers(my_token)
payload_data = utils.read_payload_file(my_file)
request_body = utils.create_payload(event_data, payload_data)
result = utils.post_request(request_headers, request_body)
```
An example successful response:
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-direct-supplier-incident-response:v2",
        "ownerId": "YOUR_OWNER_ID",
        "isErr": false,
        "errCode": "200_OK",
        "licensePlate": "qL0BJs"
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

## Next steps
You will need a mechanism to create or update your payload data whether it is stored in a file or submitted at runtime and discarded.  
You will also need a method to maintain or refer to the `processId` number of each incident.  

## Troubleshooting
Review the [troubleshooting primer](Troubleshooting.MD).
