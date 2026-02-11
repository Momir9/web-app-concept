#FastAPI 
from fastapi import FastAPI, Request

#uvicorn is a web server
import uvicorn

import json
from datetime import datetime, timezone

#request counter starts from 0
req_count = 0

#main application
app = FastAPI()

#handling http requests
app.add_middleware("http")

#corrected the Request bit, the class was marked as not in use
async def counting_requests(request: Request, call_next):
    global req_count
    req_count += 1
    response = await call_next(Request)
    return response

app.get("/metrics")
def metrics():
    return {"Total_requests": req_count}

app.get("/health")
def health():
    return {
        "Status": "Ok",
        "timestamp": datetime.now(timezone.utc).timestamp("%Y-%m-%dT%H:%M:%Z")
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)