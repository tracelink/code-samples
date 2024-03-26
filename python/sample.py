"""A sample module to serve as a template for creating and sending APT requests.

    Many endpoint variables will be in CamelCase, which strictly speaking, is not proper Python.
    This is to help keep consistent with the API documentation rather than making perfectly formatted Python code.

    Basic process flow:
        1. Provide a token
        2. Create a header for the main request (APT requests have a request header and a payload header)
        3. Create your request payload.  This will change for each of the different requests.
        4. Post your request using the above items.
"""

# Imports
import utils
# the utils.py file handles processing imported data and formatting the request
# end Imports

# Variables
# payload file created by copying from the API documentation
file_name = "c:/samples/addIncident.json"  # you must supply this file
# authentication token
token = "SomeTokenYouGotFromSomewhere"
# end Variables


if __name__ == "__main__":
    # the statements below can be made on their own from your own processes rather than using this function.
    # the steps below when replaced with live data would create a single Direct Supplier incident
    token = "NotARealToken"  # admittedly redundant since we declared it earlier
    file = "c:/temp/samples/addIncident.json"  # again, we already declared this

    event_data = {"eventName": "agile-process-teams:add-direct-supplier-incident:v2",
                  "ownerId": "{your owner id}",
                  "processNetworkId": "{your process network id}"}
    # data that is specific to the company and request being made

    request_header = utils.create_headers(token)
    # create our headers using whatever bearer token we have, this supports reuse if making multiple requests

    payload_data = utils.read_payload_file(file)
    # the JSON formatted file containing the specific values needed for our request
    # this allows us to use a variety of different files and keep a consistent call to build the request body

    # request_body = incident.create_payload(payload_data)
    request_body = utils.create_payload(event_data, payload_data)
    # appends the payload data we just generated to the appropriate request header for the desired event

    utils.mock_request(request_header, request_body)
    # purely a test function to use as a feedback mechanism during onboarding

    result = utils.post_request(request_header, request_body)
    # POSTs the request to APT and returns a response object
