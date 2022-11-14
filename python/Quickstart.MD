# APT-SCWM API Quickstart

This quickstart covers:

1. Creating a direct supplier incident using the APT-SCWM API
2. Using the response data to add a comment to the created incident   

## Request Body

For this example, we are working backwards from the request body. In its simplest form, the request body contains a header and a payload.  A simple request body resembles the following:
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
        "aptBusinessObjectSummary": "Raw materials shortage at Location XYZ",
        "directSupplierImpact": {
            "businessPriority": "MEDIUM"
        }
    }
}
```

Many requests share common values in the header. The `headerVersion`, `appName`, and `dataspace` do not change. For a single company, the `ownerId` and `processNetworkId` values are likely to remain the same. This means you may only need to determine the `eventName`. The payload will change with each new request depending on the selected `eventName`. As the integrator, you can store these values after creation or generate and use them dynamically at runtime.  

### Create Payload File

The APT-SCWM API uses JSON for passing data. The minimum required data to submit a direct supplier incident is a summary of the incident and an impact priority level.  An example of the minimum required payload:
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

However, for this example, we will include more than the miniumum information. Create a payload file containing the below and name it `addIncident.json`.  
```
{
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

The `utils.py` file has functions to help build the payload for your request body. The `read_payload_file(filename)` function reads the contents of the file, loads it into a JSON object, and does some minor processing for insertion into the request body.

In your Python terminal, enter the following:  
```
>>> import utils
>>> my_file = 'addIncident.json'
>>> payload_data = utils.read_payload_file(my_file)
```
If you already use a JSON payload as part of your other processes, you can the `accept_json_payload(payload_in)` function instead. This function accepts a JSON object, checks for proper format, and does some minor processing for insertion into the request body.

In the Python terminal, enter the following:
```
>>> my_json_data = result_from_some_other_process()
>>> payload_data = utils.accept_json_payload(my_json_data)
```

### Header

Now that you have usable payload data, you need to inform APT how to process the payload.  

In your Python terminal, enter the following, replacing values with your own:
```
>>> event_data = {"eventName": "agile-process-teams:add-direct-supplier-incident:v2",
                  "ownerId": "REPLACE_WITH_YOURS",
                  "processNetworkId": "REPLACE_WITH_YOURS"}
```
This dictionary is passed in as a parameter to the `utils.create_payload(event_in, payload_in)` function.  This function places the header and payload JSON items properly in the request body.  

Please note there is no error handling logic in these samples, you need to create your own.

Now, create the full request body. In your Python terminal, enter the following:
```
>>> request_body = utils.create_payload(event_data, payload_data)
```

## Request Header

The `utils.py` file provides a function to create a request header that can be reused until token expiration.  

In your Python terminal, enter the following:  
```
>>> my_token = however_you_get_your_token()
>>> my_header = utils.create_headers(my_token)
>>> my_header
{'Authorization': 'Bearer tokenhere', 'Content-Type': 'application/json'}
```

## Preview Request

If you wish to check your request prior to sending it, the `utils.py` file has a mock request function that will print your payload in formatted JSON, making it easier to check against the API documentation.

In your Python terminal, enter the following:  
```
>>> utils.mock_request(request_header, request_body)
HTML request header:
{'Authorization': 'Bearer my_token', 'Content-Type': 'application/json'}
Body of event request:
{
    "header": {
        "appName": "agile-process-teams",
        "dataspace": "default",
        "eventName": "agile-process-teams:add-direct-supplier-incident:v2",
        "headerVersion": 1,
        "ownerId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
        "processNetworkId": "945feb8e-09a7-4fef-9a8a-b3c5b56f87d"
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
>>> import utils
>>> my_file = 'addIncident.json'
>>> my_token = token_received_from_other_processes

>>> event_data = {"eventName": "agile-process-teams:add-direct-supplier-incident:v2",
                  "ownerId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
                  "processNetworkId": "945feb8e-09a7-4fef-9a8a-b3c5b56f87d"}
>>> request_headers = utils.create_headers(my_token)
>>> payload_data = utils.read_payload_file(my_file)
>>> request_body = utils.create_payload(event_data, payload_data)
>>> result = utils.post_request(request_headers, request_body)
```
An example successful response:
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-direct-supplier-incident-response:v2",
        "ownerId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
        "isErr": false,
        "errCode": "200_OK",
        "licensePlate": "qL0BJs"
    },
    "payload": {
        "id": "fd04dd70-c162-43ef-8118-539ca01de471"
    }
}
```

## Response Handling

The `id` in a successful response payload is the identifier of the created incident. Notice that the response is a string, not a JSON object. To get this identifier, enter the following in your Python terminal:
```
>>> import json
>>> response_json = json.loads(result.text)
>>> incident_id = response_json.get('payload').get('id')
```

To ensure your value stored properly, enter the following in your Python terminal:
```
>>> incident_id
'fd04dd70-c162-43ef-8118-539ca01de471'
```

## Add Incident Comment

Prepare a comment payload file called `comment_payload.json` containing the below:
```
{
	"payload": {
		"processId": "4ec1229a-d46f-4fc0-878f-188d318db55a",
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
>>> comment_payload_file = 'comment_payload.json'
>>> comment_payload = utils.read_payload_file(comment_payload_file)
>>> comment_payload
{'processId': '4ec1229a-d46f-4fc0-878f-188d318db55a', 'processType': 'directSupplierIncident', 'aptCommentBox': {'aptComment': {'commentText': 'Please provide a list of missing items and we will replace them.', 'visibilityType': 'Public'}}}
```
Your payload has been loaded properly, but the `processId` is still wrong. Use the `update()` function to change the stored value:
```
>>> comment_payload.update({"processId": "fd04dd70-c162-43ef-8118-539ca01de471"})
>>> comment_payload
{'processId': 'fd04dd70-c162-43ef-8118-539ca01de471', 'processType': 'directSupplierIncident', 'aptCommentBox': {'aptComment': {'commentText': 'Please provide a list of missing items and we will replace them.', 'visibilityType': 'Public'}}}
```
You can use the same process to change the `eventName`:
```
>>> event_data.update({"eventName": "agile-process-teams:add-comment-for-incident:v1"})
>>> event_data
{'eventName': 'agile-process-teams:add-comment-for-incident:v1', 'ownerId': '2aaeed40-3912-427e-a94f-51fd5a730345', 'processNetworkId': '61077cb2-601b-4c27-b11f-5e3910589931'}
```
The payload and event data should now be updated. You can verify this by resending the commands to build the request body and resend the request.  
```
>>> request_body = utils.create_payload(event_data, payload_data)
>>> comment_result = utils.post_reqeust(request_headers, requst_body)
```
The response:  
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-comment-for-incident-response:v1",
        "ownerId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
        "isErr": false,
        "errCode": "200_OK",
        "licensePlate": "vXPsFz"
    },
    "payload": {
        "id": "a67d7261-33b1-4be6-9760-61ae8fe9eed3"
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
       "ownerId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
       "appName": "agile-process-teams",
       "dataspace": "default",
       "processNetworkId": "945feb8e-09a7-4fef-9a8a-b3c5b56f87d"
   },
   "payload": {
       "id": "fd04dd70-c162-43ef-8118-539ca01de471"
   }
}
```
The response provides the complete record for the incident:
```
{
"header": {
	"headerVersion": 1,
	"eventName": "agile-process-teams:read-directSupplierIncident-response:v3",
	"ownerId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
	"isErr": false,
	"errCode": "200_OK",
	"licensePlate": "Y7yRFr-tRpXpc"
},
"payload": {
	"createdByUserId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
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
			"94f94f37-2772-4b39-8041-9c2dcfcfff82"
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
		"fkProcessNetworkId": "945feb8e-09a7-4fef-9a8a-b3c5b56f87d",
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
	"ownerId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
	"objectType": "agile-process-teams:directSupplierIncident",
	"currentBaseState": "Closed",
	"schemaId": "agile-process-teams:directSupplierIncident",
	"lastUpdatedByUserId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
	"contextualOwnerId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
	"id": "fd04dd70-c162-43ef-8118-539ca01de471",
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
