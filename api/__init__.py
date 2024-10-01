import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Handle preflight request (OPTIONS)
    if req.method == "OPTIONS":
        headers = {
            'Access-Control-Allow-Origin': 'https://brave-water-0dadd3a10.5.azurestaticapps.net',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Authorization, Content-Type',
            'Access-Control-Allow-Credentials': 'true'
        }
        return func.HttpResponse(status_code=204, headers=headers)

    # Handle GET request
    if req.method == "GET":
        data = {"message": "Hello World"}
        response = func.HttpResponse(
            json.dumps(data),
            mimetype="application/json",
            status_code=200
        )
        # Adding the CORS headers
        response.headers['Access-Control-Allow-Origin'] = 'https://brave-water-0dadd3a10.5.azurestaticapps.net'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    # Handle POST request
    if req.method == "POST":
        response = func.HttpResponse(
            "POST request received",
            status_code=200
        )
        # Adding the CORS headers
        response.headers['Access-Control-Allow-Origin'] = 'https://brave-water-0dadd3a10.5.azurestaticapps.net'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    # Default response for unhandled methods
    return func.HttpResponse(
        "Unhandled request method",
        status_code=400
    )
