# Working with Events in the API

Each request type in the API has a specific eventName parameter passed in to identify how to process the request.  Event names are specific to the type of operation you select.

## Event name mapping  

Some event names can be used for multiple operations within their category.  For each incident type use the identified **eventName** in your request header.  
*Consult the API documentation for more information for each of these events and their use.*

### Direct Supplier Incident  

**Create a new incident**  

- Add Direct Supplier Incident request:	**Event Name:**	```"agile-process-teams:add-direct-supplier-incident:v2"```  

**Modify an existing incident**  

- Edit Direct Supplier Incident request:	**Event Name:**	```"agile-process-teams:edit-direct-supplier-incident:v2"```  
    - Edit base state
    - Edit Partner and Impact information
    - Edit with initial response
    - Edit with final response

**Copy an existing incident to a create a new incident**  

- Copy Direct Supplier Incident request:	**Event Name:**	```"agile-process-teams:copy-direct-supplier-incident:v2"```  

**Close an existing incident**  

- Close Direct Supplier Incident request:	**Event Name:**	```"agile-process-teams:close-direct-supplier-incident:v2"```  

**Reopen a closed incident**  

- Reopen Direct Supplier Incident request:	**Event Name:**	```"agile-process-teams:reopen-direct-supplier-incident:v1"```  

**Submit an incident to a partner**  

- Submit Direct Supplier Incident to Partner request:	**Event Name:**	```"agile-process-teams:submit-direct-supplier-incident-to-partner:v1"```  

### Indirect Supplier Incident  

**Create a new incident**  

- Add Indirect Supplier Incident request:	**Event Name:**	```"agile-process-teams:add-indirect-supplier-incident:v2"```  

**Modify an existing incident**  

- Edit Indirect Supplier Incident request:	**Event Name:**	```"agile-process-teams:edit-indirect-supplier-incident:v2"```  

    - Edit base state
    - Edit Partner and Impact information
    - Edit with initial response
    - Edit with final response

**Copy an existing incident to a create a new incident**  

- Copy Indirect Supplier Incident request:	**Event Name:**	```"agile-process-teams:copy-indirect-supplier-incident:v2"```  

**Close an existing incident**  

- Close Indirect Supplier Incident request:	**Event Name:**	```"agile-process-teams:close-indirect-supplier-incident:v2"```  

**Reopen a closed incident**  

- Reopen Indirect Supplier Incident request:	**Event Name:**	```"agile-process-teams:reopen-indirect-supplier-incident:v1"```  

**Submit an incident to a partner**  

- Submit Indirect Supplier Incident to Partner request:	**Event Name:**	```"agile-process-teams:submit-indirect-supplier-incident-to-partner:v1"```  

### External Manufacturing Incident  

**Create a new incident**  

- Add External Manufacturing Incident request:	**Event Name:**	```"agile-process-teams:add-external-manufacturing-incident:v2"```  

**Modify an existing incident**  

- Edit External Manufacturing Incident request:	**Event Name:**	```"agile-process-teams:edit-external-manufacturing-incident:v2"```  

    - Edit base state
    - Edit Partner and Impact information
    - Edit with initial response
    - Edit with final response

**Copy an existing incident to a create a new incident**  

- Copy External Manufacturing Incident request:	**Event Name:**	```"agile-process-teams:copy-external-manufacturing-incident:v1"```  

**Close an existing incident**  

- Close External Manufacturing Incident request:	**Event Name:**	```"agile-process-teams:close-external-manufacturing-incident:v2"```  

**Reopen a closed incident**  

- Reopen External Manufacturing Incident request:	**Event Name:**	```"agile-process-teams:reopen-external-manufacturing-incident:v1"```  

**Submit an incident to a partner**  

- Submit External Manufacturing Incident to Partner request:	**Event Name:**	```"agile-process-teams:submit-external-manufacturing-incident-to-partner:v1"```  

### Internal Manufacturing Incident  

**Create a new incident**  

- Add Internal Manufacturing Incident request:	**Event Name:**	```"agile-process-teams:add-internal-manufacturing-incident:v2"```  

**Modify an existing incident**  

- Edit Internal Manufacturing Incident request:	**Event Name:**	```"agile-process-teams:edit-internal-manufacturing-incident:v2"```  

    - Edit base state
    - Edit Impact information
    - Edit with initial response
    - Edit with final response

**Copy an existing incident to a create a new incident**  

- Copy Internal Manufacturing Incident request:	**Event Name:**	```"agile-process-teams:copy-internal-manufacturing-incident:v1"```  

**Close an existing incident**  

- Close Internal Manufacturing Incident request:	**Event Name:**	```"agile-process-teams:close-internal-manufacturing-incident:v2"```  

**Reopen a closed incident**  

- Reopen Internal Manufacturing Incident request:	**Event Name:**	```"agile-process-teams:reopen-internal-manufacturing-incident:v1"```  

### Shared Incident operations  

**Add a new comment to an incident**

- Add Comment For Incident request:	**Event Name:**	
```"agile-process-teams:add-comment-for-incident:v1"```  

**Edit an existing comment**

- Edit Comment For Incident request:	**Event Name:**	
```"agile-process-teams:edit-comment-for-incident:v1"```  

**List the comments for an incident**

- List Comments For Incident request:	**Event Name:**	```"agile-process-teams:list-comments-for-incident:v1"```  

**Follow or unfollow an incident**

- Toggle User Follows Incident request:	**Event Name:**	```"agile-process-teams:toggle-user-follows-incident:v1"```  

**Get the activity history for an incident**

- Get Activity History For Incident request:	**Event Name:**	```"agile-process-teams:get-activity-history-for-incident:v1"```  

*These event names are also available in JSON format in the eventNames.json file for use in code solutions.*

# Next  

Work through a simple tutorial in the [Using the API walk-through](UsingTheAPI.MD) guide.  
