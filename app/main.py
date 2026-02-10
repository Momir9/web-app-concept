from fastapi import FastAPI, Request
import uvicorn
import json
from datetime import datetime

req_count = 0 #request counter starts from 0
app = FastAPI

app.add_middleware(FastAPI)
async def counting_requests(Request, call_next):
    global req_count
    req_count += 1
    response = await call_next()
    return response

def metrics():
    return {"total_requests": req_count}

app.get("/health")
def health():
    return.json {"status": "ok", "timestamp": ""}
    #timestamp = ('%Y-%m-%dT%H:%M:%Z')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)