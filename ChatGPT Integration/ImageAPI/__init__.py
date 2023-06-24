import logging

import azure.functions as func
import openai

secret_key = 'your api key'

#Sample
# {"prompt":"Goku wating in airport", "n":1, "size":"1024x1024"}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # set api key
    openai.api_key = secret_key

    # get variable from the http request body
    req_body = req.get_json()
    logging.info(type(req_body))

    # output
    output = openai.Image.create(
            prompt=req_body["prompt"],
            n=req_body["n"],
            size=req_body["size"]
        )
    return func.HttpResponse(f"{output['data'][0]['url']}", status_code=200)