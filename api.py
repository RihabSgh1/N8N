from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    data: dict

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI example"}

@app.post("/postdata")
def post_data(item: Item):
    return {"received_data": item.data}
