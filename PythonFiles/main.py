from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from joblib.testing import param

app = FastAPI()


@app.get("/")
async def handler(request: Request):
    payload = await request.json()

    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if intent == "track.order - context:onngoing-tracking":
        return JSONResponse(content={
            "fulfillmentMessage": f"Received =={intent}== in the backend"
        })

def track_order()