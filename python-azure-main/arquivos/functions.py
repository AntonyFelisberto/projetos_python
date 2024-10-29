import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpTrigger")
def httpTrigger(req:func.HttpRequest)->func.HttpResponse:
    logging.info("Python HTTP trigger")

    name = req.params.get("name")
