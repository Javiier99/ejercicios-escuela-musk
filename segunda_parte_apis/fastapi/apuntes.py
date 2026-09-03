

# from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app =  FastAPI()

@app.get("/")
def read_root() -> dict:
    return {"mensaje" : "Hola Caracola"}


@app.get("/items/{item_id}")
def read_items(item_id):
    if item_id == 0:
        return JSONResponse(status_code=404, content={"mesaje" : "Item no found"})
    return {"Item" : item_id}





