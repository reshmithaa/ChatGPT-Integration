import logging

import azure.functions as func
# pip install opeanai
import openai

secret_key = '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'

#Sample
# {"model":"text-davinci-003", "prompt":"Tell a boy name", "max_tokens":200, "temperature":0}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # set api key
    openai.api_key = secret_key

    # get variable from the http request body
    req_body = req.get_json()
    logging.info(type(req_body))

    # output
    output = openai.Completion.create(
        model=req_body["model"],
            prompt=req_body["prompt"],
            max_tokens=req_body["max_tokens"],
            temperature=req_body['temperature']
        )
    return func.HttpResponse(f"{output.choices[0]['text']}", status_code=200)