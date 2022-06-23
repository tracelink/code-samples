# TraceLink Opus Agile Process Teams (APT) developer knowledge base  

## Python development samples  

**Communicating with the Agile Process Teams Supply Chain Issue Management (APT-SCIM) application using Python.**

**Tested for use with Python version 3.10.**  
**The *requests* and *json* modules are required for use.**  
Use the **utils.py** file for the following actions:  

- Add your token to the HTTP request header  
- Process the request payload from a JSON object or file  
- Create the payload body  
- Display the completed payload for accuracy prior to submitting  
- Submit your request to Agile Process Teams  

### All requests contain three basic items  

- **A request URL**
	- {{protocol}}://{{server}}/api/events  
- **A request header**
	- Generated using a token and a content type *(usually 'application/json')*.
- **A payload**
	- *All APT requests contain a request header **AND** a payload header*.

The request header provides authentication with the APT application.  
The payload header provides information needed to properly route the request.

The samples provided show the minimum required or commonly used payload data and provide a method for specifying parameters for header and payload data.  
Each event folder also contains a *samples* folder with payload template files properly formatted with sample payload data.

# Next  

[Basic request formatting](FormatRequests.MD) - Learn the request body requirements  
[Event name mapping](EventNames.MD) - Shows the event name text to use in the header for each request type  
[Using the API walk-through](UsingTheAPI.md) - A simple walk-through example  