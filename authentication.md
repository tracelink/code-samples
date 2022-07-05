# Authentication 

## Prerequisites 

You must be able to login to the Opus Platform and access APT-SCWM. 

Once logged into Opus on your browser, select the desired process. For example, Direct Supplier Incident. 

You will need the values for the following keys: 

1. `_store_js_production_processNetworkOwnerId`
2. `_store_js_production_processNetworkId`
3. `_store_js_production_token`

Use the directions for your browser below to generate these values.

### Chrome

From the Chrome menu, navigate to **View** > **Developer** > **Developer Tools**.
Select the **Application** tab from the Developer Tools pane. From the left hand navigation menu, under the storage section, select
**Local Storage** from the dropdown. Then, click `https://opus.tracelink.com`. You should now see a list of key/value pairs. 

### Firefox

From the Firefox menu, navigate to **Tools** > **Web Developer Tools**.
Select the **Storage** tab from the Web Developer Tools pane. From the left hand navigation menu, click **Local Section** and then
`https://opus.tracelink.com`. You should now see a list of key/value pairs. 

##Generate API Key

###Postman

1. Set up a POST call to `https://valvir-opus.tracelink.com/api/events`.
2. Under the **Authorization** tab select **Bearer Token** as the **Type** and insert the `_store_js_production_token` obtained
from your broswer as the **Token**. 
3. Use exact json below as the payload body. You do not need to replace any values here. 

```json
{
    "payload": {
        "description": "descJ100"
    },
    "header": {
        "dataspace": "default",
        "appName": "user-admin",
        "headerVersion": 1,
        "eventName": "authorization-manager:generate-apiKeyCredentials:v1",
        "ownerId": "00000000-0000-0000-0000-000000000000"
    }
}
```

Here is an example of the response you should receive: 

```json
{
  "header": {
    "headerVersion": 1,
    "eventName": "authorization-manager:generate-apiKeyCredentials-response:v1",
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "isErr": false,
    "errCode": "200_OK",
    "licensePlate": "lrYvpv-0Cj4nC"
  },
  "payload": {
    "apiKey": "10e1c36c-2f49-46f3-b552-e28b5d671b5f",
    "apiSecret": "jt3x1xz0LxLbRyMhPMuuObbabnNxbpFk"
  }
}
```
