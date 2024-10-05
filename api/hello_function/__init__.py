import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        "Hello, this is a simple function for enabling Application Insights!",
        status_code=200
    )