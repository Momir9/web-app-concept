from fastapi import FastAPI, Request

#uvicorn web server
import uvicorn
from datetime import datetime, timezone

#request counter starts from 0
req_count = 0

#main application
app = FastAPI()

#handling http requests
@app.middleware("http")
async def counting_requests(request: Request, call_next):
    global req_count
    req_count += 1
    response = await call_next(request)
    return response

@app.get("/metrics")
def metrics():
    return {"Total_requests": req_count}

@app.get("/health")
def health():
    return {
        "Status": "Ok",
        #need to use strftime instead of .timestamp
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%Z")
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)