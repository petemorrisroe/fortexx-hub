import azure.functions as func
from fasthtml.common import serve

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("Simple Azure Function Trigger", status_code=200)

if __name__ == "__main__":
    serve()
