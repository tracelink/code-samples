# Working with Events

Event names are specific to selected operation and passed as the `eventName` in your request header.

## Event names 

Please reference [API documentation](https://opus.tracelink.com/documentation/2021.1/en-US/apt/Content/topics/api/landing_incident_apis.htm?tocpath=Set%20up%20APIs%7CIncident%20process%20APIs%7C_____0) for more information on each event type.

### Direct Supplier Incident  

| **Action**                                     | **Event Name**                                                      |
| ---------------------------------------------- | ------------------------------------------------------------------- |
| Create a new incident                          | `"agile-process-teams:add-direct-supplier-incident:v2"`             |
| Modify an existing incident                    | `agile-process-teams:edit-direct-supplier-incident:v2`              |
| Copy existing incident and create new incident | `agile-process-teams:copy-direct-supplier-incident:v2`              |
| Close an existing indicent                     | `agile-process-teams:close-direct-supplier-incident:v2`             |
| Reopen a closed incident                       | `agile-process-teams:reopen-direct-supplier-incident:v1`            |
| Submit an incident to a partner                | `agile-process-teams:submit-direct-supplier-incident-to-partner:v1` | 

### Indirect Supplier Incident

| **Action**                                     | **Event Name**                                                        |
| ---------------------------------------------- | --------------------------------------------------------------------- |
| Create a new incident                          | `agile-process-teams:add-indirect-supplier-incident:v2`               |
| Modify an existing incident                    | `agile-process-teams:edit-indirect-supplier-incident:v2`              |
| Copy existing incident and create new incident | `agile-process-teams:copy-indirect-supplier-incident:v2`              |
| Close an existing indicent                     | `agile-process-teams:close-indirect-supplier-incident:v2`             |
| Reopen a closed incident                       | `agile-process-teams:reopen-indirect-supplier-incident:v1`            |
| Submit an incident to a partner                | `agile-process-teams:submit-indirect-supplier-incident-to-partner:v1` | 
  

### External Manufacturing Incident  

| **Action**                                     | **Event Name**                                                             |
| ---------------------------------------------- | -------------------------------------------------------------------------- |
| Create a new incident                          | `agile-process-teams:add-external-manufacturing-incident:v2`               |
| Modify an existing incident                    | `agile-process-teams:edit-external-manufacturing-incident:v2`              |
| Copy existing incident and create new incident | `agile-process-teams:copy-external-manufacturing-incident:v1`              |
| Close an existing indicent                     | `agile-process-teams:close-external-manufacturing-incident:v2`             |
| Reopen a closed incident                       | `agile-process-teams:reopen-external-manufacturing-incident:v1`            |
| Submit an incident to a partner                | `agile-process-teams:submit-external-manufacturing-incident-to-partner:v1` | 


### Internal Manufacturing Incident 

| **Action**                                     | **Event Name**                                                             |
| ---------------------------------------------- | -------------------------------------------------------------------------- |
| Create a new incident                          | `agile-process-teams:add-internal-manufacturing-incident:v2`               |
| Modify an existing incident                    | `agile-process-teams:edit-internal-manufacturing-incident:v2`              |
| Copy existing incident and create new incident | `agile-process-teams:copy-internal-manufacturing-incident:v1`              |
| Close an existing indicent                     | `agile-process-teams:close-internal-manufacturing-incident:v2`             |
| Reopen a closed incident                       | `agile-process-teams:reopen-internal-manufacturing-incident:v1`            |


### Comments & Activities

| **Action**                           | **Event Name**                                             |
| ------------------------------------ | ---------------------------------------------------------- |
| Add comment to an incident           | `agile-process-teams:add-comment-for-incident:v1`          |
| Edit comment for an indcident        | `agile-process-teams:edit-comment-for-incident:v1`         |
| List comments for an incident        | `agile-process-teams:list-comments-for-incident:v1`        |
| Follow or unfollow an incident       | `agile-process-teams:toggle-user-follows-incident:v1`      |
| Get activity history for an incident | `agile-process-teams:get-activity-history-for-incident:v1` |    

# Next  

Follow the [tutorial](Tutorial.MD) for an example using the APT API.  
