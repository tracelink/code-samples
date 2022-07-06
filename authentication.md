# Authentication 

## Prerequisites 

1. You must be able to login to the Opus Platform and access APT-SCWM. 

2. Once logged into Opus on your browser, select the desired process. For example, Direct Supplier Incident. 

![Opus in Browser](images/opus_apt.png)

3. Using the directions below for your designated, generate the following values:

- `_store_js_production_processNetworkOwnerId`
- `_store_js_production_processNetworkId`
- `_store_js_production_token`

### Chrome

From the Chrome menu, navigate to **View** > **Developer** > **Developer Tools**.
Select the **Application** tab from the Developer Tools pane. From the left hand navigation menu, under the storage section, select
**Local Storage** from the dropdown. Then, click `https://opus.tracelink.com`. You should now see a list of key/value pairs. 

![Key Value Pairs](images/chrome_apt.png)

### Firefox

From the Firefox menu, navigate to **Tools** > **Web Developer Tools**.
Select the **Storage** tab from the Web Developer Tools pane. From the left hand navigation menu, click **Local Section** and then
`https://opus.tracelink.com`. You should now see a list of key/value pairs. 

## Generate API Key and Secret

### Postman

1. Set up a POST call to `https://valvir-opus.tracelink.com/api/events`.
2. Under the **Authorization** tab select **Bearer Token** as the **Type** and insert the `_store_js_production_token` obtained
from your broswer as the **Token**. 

![Postman Token](images/postman_token.png)

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

The API key and secret long-lived, static values that do not expire. 

## Encode API Key and Secret

In order to make an API call using your API key and secret, they will need to be base64 encoded.

Use the format {{KEY}}:{{SECRET}}, where a colon is separating the two values. Using the response values above as an example,
`10e1c36c-2f49-46f3-b552-e28b5d671b5f:jt3x1xz0LxLbRyMhPMuuObbabnNxbpFk`.

Use the following command in your terminal window:
`echo -n 'KEYSECRETSTRING' | base64`

The result will look like this:
`MTBlMWMzNmMtMmY0OS00NmYzLWI1NTItZTI4YjVkNjcxYjVmOmp0M3gxeHowTHhMYlJ5TWhQTXV1T2JiYWJuTnhicEZr`

Alternatively you can use an online resource such as https://www.base64encode.org/.

This value can now be used in a basic authorization header. For example,
`authorization: Basic NGFiZjAyMjItZmU…M3Y2ZzFvZEFPQ1F5RUFKSkI3TWpNOFRFNVpw`.


