# test_server.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Sample POST request model (optional for /test/)
class TestModel(BaseModel):
    message: str = "Hello"

# GET endpoint (can test in browser)
@app.get("/test/")
def test_get():
    return {"status": "ok-get"}

# POST endpoint (can test in Postman)
@app.post("/test/")
def test_post(data: TestModel = None):
    return {"status": "ok-post", "received": data.dict() if data else None}


