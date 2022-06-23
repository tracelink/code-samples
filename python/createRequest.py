import json
from utils import event_data  # reusable values identifying the ownerId and processNetworkId if not built dynamically


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
                "eventName": event_in.get('event_name'),
                "ownerId": event_in.get('ownerId'),
                "processNetworkId": event_in.get('processNetworkId'),
                "appName": "agile-process-teams",
                "dataspace": "default"
            },
            "payload": payload_in
        }
    )
    return payload
