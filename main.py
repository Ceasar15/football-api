from fastapi import FastAPI
from typing import Optional
from api.endpoints import endpoint
from users import api




app = FastAPI()
app.include_router(endpoint.router)
app.include_router(api.router)


@app.get("/")
def home():
    return {"getting": "started"}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
