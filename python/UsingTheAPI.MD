# How to use the Agile Process Teams API  
In this section, we will work through the basic steps of creating a direct supplier incident using the Agile Process Teams API and reusing the response data to add a comment to the same incident.  

## The situation  
Your task is to automate the processes related to working with Agile Process Teams for Supply Chain Issue Management (APT-SCIM).  While your section has a small staff dedicated to working with the TraceLink interface, your company still has some internal processes required for quality control.  One of these is a form-based tracking system on your intranet that is used to monitor quality and efficiency.  

Since you created most of the form's inner workings, you have an opportunity to consolidate some effort.  Depending on how your system communicates, you could even create a JSON object on demand and supply it to APT programmatically.  

In this case, your team leveraged Python since it's commonly used in your environment.  

## Anatomy of a request body
In its simplest form, an Agile Process Teams request body has two main items: a **header** and a **payload**.  A simple request body resembles the following:
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-direct-supplier-incident:v3",
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
Many requests share common data items in the header of the request body.  For a single company, the *ownerId* and *processNetworkId* values may not change.  This leaves only the *eventName* item that would change with each type of request.  

The payload will change entirely with each new request type.  As the integrator, you have the option of storing these values after creation or generating and using them dynamically at runtime.  

## Determine the data you will need to create the incident  
For this example, we are working backwards from the request payload.  The order in which you create your data is not important.  The body of the request is created in a single statement once all required elements are available.  

The Agile Process Teams API uses JavaScript Object Notation (JSON) for passing data.  After reviewing the API documentation, you realize your existing system can create your JSON files with a few minor adjustments.  

The absolute minimum data required to submit a direct supplier incident is a summary of the incident and an impact priority level.  This minimal payload would look like this:  
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
## Create your first request
You decide to start small with a test case.  In this situation, you decide to create a simple incident as a test; you could update the incident with more meaningful data later or just close it and move on.  

### The payload
Not satisfied to do the minimum, you decide to add just a bit more information for your first run.  After consulting the API documentation to make sure you have the requirements met, you create a payload file below and name it **addIncident.json**.  
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
The **utils.py** file has functions to help build the payload for your request body:  
**read_payload_file(filename)** - This function reads the contents of the file, loads it into a JSON object, and does some minor processing for insertion into the request body.  
In the Python terminal, you enter the following:  
```
>>> import utils
>>> my_file = 'addIncident.json'
>>> payload_data = utils.read_payload_file(my_file)
```
If you already use a JSON payload as part of your other processes, you can use another provided function:  
**accept_json_payload(payload_in)** - This function accepts a JSON object, checks for proper format, and does some minor processing for insertion into the request body.  

In the Python terminal, it could look something like this  
```
>>> my_json_data = result_from_some_other_process()
>>> payload_data = utils.accept_json_payload(my_json_data)
```
There is no magic happening in the **utils.py** file.  The Developer Relations team has put together a few simple functions to make learning how to work with the API a bit simpler.  You can use these functions as a guide or write your own functions that are more suitable for your needs.  

### The request header
Now that we have usable payload data, we need to inform APT how to process the payload.  
To do this we need to declare some values for use in the header of our request body.   
You return to your open Python terminal and enter the following:  
```
>>> event_data = {"eventName": "agile-process-teams:add-direct-supplier-incident:v3",
                  "ownerId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
                  "processNetworkId": "945feb8e-09a7-4fef-9a8a-b3c5b56f87d"}
```
This dictionary is passed in as a parameter to the *utils.create_payload(event_in, payload_in)* function.  This function places the header and payload JSON items properly in the request body.  

***Note: There is no error handling logic in these samples, you need to create your own.***

With this *event_data* dictionary created, you're ready to create the full request body in your existing Python terminal.  
```
>>> request_body = utils.create_payload(event_data, payload_data)
```
You can refer to the API document and verify your output to the prescribed template your first few times to validate your processes are working properly.  

### Your token  
Review the Opus API getting started readme for a refresher to generate or obtain the token required to send your requests.  Be mindful that tokens may expire at different intervals, so plan your integration accordingly.  

### The HTTP request header  
You provide your token as part of your authorization to make requests to APT.  This can be done separately if multiple requests are sent in succession, or as part of the final request build prior to sending.  The **utils.py** file in our examples provides function to create a request header that can be reused until token expiration.  
In the Python terminal, it could look something like this  
```
>>> my_token = however_you_get_your_token()
>>> my_header = utils.create_headers(my_token)
>>> my_header
{'Authorization': 'Bearer not a real token', 'Content-Type': 'application/json'}
```

### Preview your request
If you wish to check your request prior to sending it, the **utils.py** file has a mock request function that will print your payload in 'pretty JSON' making it easier to check against the API documentation.  
Simply use the following call:  
```
>>> utils.mock_request(request_header, request_body)
HTML request header:
{'Authorization': 'Bearer my_token', 'Content-Type': 'application/json'}
Body of event request:
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

## Completing and sending your request  
You're ready to submit your request when you have the following created:
	- A request header.  ex: {'Authorization': 'Bearer my_token', 'Content-Type': 'application/json'}  
	- A request body.  ex: {"header": {event headers}, "payload": {your generated payload}}  
The **utils.py** file contains a function to help send your request and capture the response.  You're free to use your own methods if your needs differ.
An example Python terminal session from start to finish could look like this:
```
>>> import utils
>>> my_file = 'addIncident.json'
>>> my_token = token_received_from_other_processes

>>> event_data = {"eventName": "agile-process-teams:add-direct-supplier-incident:v3",
                  "ownerId": "94f94f37-2772-4b39-8041-9c2dcfcfff82",
                  "processNetworkId": "945feb8e-09a7-4fef-9a8a-b3c5b56f87d"}
>>> request_headers = utils.create_headers(my_token)
>>> payload_data = utils.read_payload_file(my_file)
>>> request_body = utils.create_payload(event_data, payload_data)
>>> result = utils.post_request(request_headers, request_body)
```
A successful request would return a response similar to:
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-direct-supplier-incident-response:v3",
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

## Handling your results
The 'id' in a successful response payload will be the identifier of the incident you created.  You need to get the text of your response object, so don't forget to reference that part specifcially.  Notice that our response is a string, not a JSON object.  You will need this identifier later so you enter the following in your terminal:
```
>>> import json
>>> response_json = json.loads(result.text)
>>> incident_id = response_json.get('payload').get('id')
```
And you check to make sure your value stored properly by referencing the incident_id in your terminal:
```
>>> incident_id
'fd04dd70-c162-43ef-8118-539ca01de471'
```
Simply referencing the variable in your terminal, Python will immediately respond with just the value in single quotes.  

### Reusing your result data for another request
You decide to add a comment during the same session to test the process.  You've prepared a comment payload file that looks like this:
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
But you notice that your id number placeholder does not match.  You can load your comment file and update the id number dynamically.  
You return to your Python terminal:
```
>>> comment_payload_file = 'comment_payload.json'
>>> comment_payload = utils.read_payload_file(comment_payload_file)
>>> comment_payload
{'processId': '4ec1229a-d46f-4fc0-878f-188d318db55a', 'processType': 'directSupplierIncident', 'aptCommentBox': {'aptComment': {'commentText': 'Please provide a list of missing items and we will replace them.', 'visibilityType': 'Public'}}}
```
Your payload has been loaded properly, but the id is still wrong.  You can use the update() function to change the value stored in the 'id' key.
```
>>> comment_payload.update({"processId": "fd04dd70-c162-43ef-8118-539ca01de471"})
>>> comment_payload
{'processId': 'fd04dd70-c162-43ef-8118-539ca01de471', 'processType': 'directSupplierIncident', 'aptCommentBox': {'aptComment': {'commentText': 'Please provide a list of missing items and we will replace them.', 'visibilityType': 'Public'}}}
```
You can use the same process to change your eventName to use the comment event name:
```
>>> event_data.update({"eventName": "agile-process-teams:add-comment-for-incident:v1"})
>>> event_data
{'eventName': 'agile-process-teams:add-comment-for-incident:v1', 'ownerId': '2aaeed40-3912-427e-a94f-51fd5a730345', 'processNetworkId': '61077cb2-601b-4c27-b11f-5e3910589931'}
```
You now have updated payload and event data.  You decide to test this by resending the commands to build the request body and resend the request.  
```
>>> request_body = utils.create_payload(event_data, payload_data)
>>> comment_result = utils.post_reqeust(request_headers, requst_body)
```
Sending this request, you find that your hard work has paid off.  
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

## Next steps
You will need a mechanism to create or update your payload data whether it's stored in a file or submitted at runtime and discarded.  
You will also need a method to maintain or refer to the id number of specific incidents.  

#### Not working as expected?
See our [troubleshooting primer](Troubleshooting.MD) for hints to get you started.
