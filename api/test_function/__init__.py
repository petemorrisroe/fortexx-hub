import logging
import azure.functions as func

async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing request for test function')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}!", status_code=200)
    else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body",
            status_code=400
        )
