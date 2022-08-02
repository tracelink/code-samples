# This utils file is meant as a primer only.  There is no error handling built in

import requests
import json

# establish some variables
# This is a placeholder for event data, it can be used to hold data as needed or (more likely) built during runtime.
# Be careful with the eventName.  It should change depending on the category of  request.
event_data = {
    "eventName": "agile-process-teams:add-direct-supplier-incident:v2",
    "ownerId": "{your ownerId}",
    "processNetworkId": "{your processNetworkId}"
}

# we expect this to remain static
request_url = "URL provided by your administrator"


def read_payload_file(filename):
    """
    Opens a JSON formatted file and attempts to create a JSON payload object to submit to the specified module.

    :param filename: Path to a file containing the JSON formatted payload data.
    :return: Reformatted payload data ready to be appended to a request body.
    """
    try:
        with open(filename, 'r') as file_in:
            data = file_in.read()
        j_object = json.loads(data)
        my_payload = j_object.get("payload")  # we're parsing inside the 'payload' node to just get the payload data
        return my_payload
    except Exception as e:
        print(e)


def accept_json_payload(payload_in):
    """
    Receives the already-formatted JSON string portion of the payload and prepares it for submission.

    :param payload_in: string - Formatted JSON string with payload data.
    :return: Reformatted payload data ready to be appended to a request body.
    """
    try:
        # check to see if the payload is a valid JSON string, the application will reject bad data
        data = json.loads(payload_in)
        payload = data.get("payload")
        return payload
    except ValueError as v:
        print("JSON formatted string not found: {}.  Please check formatting and resubmit".format(v))
    except Exception as e:
        print("Unexpected exception: {}.".format(e))


def create_headers(method, token):
    """
    Takes a token and returns a formatted request header (excluding the URL)
    :param method: string - Basic or Bearer
    :param token: string - Authentication token formatted as a string.
    :return: Dictionary object containing the Authorization and Content Type
    """
    headers = {"Authorization": "{0} {1}".format(method, token), "Content-Type": "application/json"}
    return headers


def create_payload(event_in, payload_in):
    """
    Takes a JSON payload object in and combines it with the appropriate header for the request.

    The API documentation outlines the available fields and data types for each request.

    The request body payload section can be generated dynamically or written to a file and parsed by the utils.read_json_file() function.

    :param event_in: string: A JSON object with the event name, owner id, process network id (to create request body header)
    :param payload_in: string: Should be a properly formatted JSON object prescribed by the API documents
    :return: A completed request body
    """
    payload = json.dumps(
        {
            "header": {
                "headerVersion": 1,
                "eventName": event_in.get('eventName'),
                "ownerId": event_in.get('ownerId'),
                "processNetworkId": event_in.get('processNetworkId'),
                "appName": "agile-process-teams",
                "dataspace": "default"
            },
            "payload": payload_in
        }
    )
    return payload


def mock_request(header, data):
    """
    Test function to allow the user to compare their generated request body without sending it to APT.

    This is a learning tool only intended to allow the user to verify the data they generate against the official
    Agile Process Teams API documentation to verify they have constructed a properly formatted payload.

    This function DOES NOT communicate with APT to verify required data or correct id numbers.

    :param header: dict - Header with token and content type
    :param data: str - JSON string with the completed request body
    :return: Outputs a 'pretty print' of the JSON request body for comparison to the API documentation
    """
    
    # reloading in the parsed data to do a JSON pretty print
    request_body = json.loads(data)
    print("HTML request header:")
    print(header)
    print("Body of event request:")
    print(json.dumps(request_body, indent=4, sort_keys=True))
    return


def post_request(header, data):
    """
    Takes a request URL, headers, and payload and submits the request to Opus APT

    :param header: dict:
        Provide a token as a string to the create_headers function.
        The output is your request header.
    :param data: string:
        The payload required for the endpoint to be used.
        Each module will produce its own payload that can be passed as the data parameter.
    :return: Response object with status code and message
    """
    # we expect the URL to remain static for APT, so we'll just keep it in here as a variable
    url = request_url

    # actually sending the request
    response = requests.request("POST", url, headers=header, data=data)

    # process the response and inform the user
    print("Response status code: {0}".format(response.status_code))
    print("Response message {0}".format(response.text))
    return response
