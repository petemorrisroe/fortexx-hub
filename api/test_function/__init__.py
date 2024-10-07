import logging
import azure.functions as func

async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(
        "I'm alive!",
        status_code=200
    )

