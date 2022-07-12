# TraceLink Opus Platform: Agile Process Teams

This repository provides developers with python code samples for interacting with TraceLink's Agile Process Teams (APT) app.

## Python

This code was tested using python 3.10.0.

**The *requests* and *json* modules are required for use.**
Use the **utils.py** file for the following actions:  

- Add your token to the HTTP request header  
- Process the request payload from a JSON object or file  
- Create the payload body  
- Display the completed payload for accuracy prior to submitting  
- Submit your request to Agile Process Teams  

### Requests

All requests have three main components: 

- **A request URL**
	- {{protocol}}://{{server}}/api/events  
- **A request header**
	- Authenticates to APT using a token and content type.
- **A payload**
	- *All APT requests contain a request header **AND** a payload header*.

The payload header provides information needed to properly route the request.

The samples provided *(in the payload-samples folder)* show the minimum required or commonly used payload data and provide a method for specifying parameters for header and payload data.  These sample files contain only the payload section for clarity.  Longer versions of these samples are available on the API documentation pages.  

# Next  

[Basic request formatting](FormatRequests.MD) - Learn the request body requirements  
[Event name mapping](EventNames.MD) - Shows the event name text to use in the header of each request type  
[Using the API walk-through](UsingTheAPI.MD) - A simple walk-through example  
[Troubleshooting primer](Troubleshooting.MD) - A basic troubleshooting example  