import uvicorn
from fastapi import FastAPI
from data import data_load, data
from pydantic import BaseModel
# from typing import Union



class Item(BaseModel):
    name: str
    weight: int


app = FastAPI()


@app.get("/dragon/{id}")
async def get_dragon(id: int):
    dragon_data: dict = data_base["dragon"]
    if id in dragon_data.keys():
        return dragon_data[id]
    else:
        return {id: "not found"}


@app.patch("/dragon/{id}")
async def change_dragon(id: int, item: Item):
    dragon_data: dict = data_base["dragon"]
    if id in dragon_data.keys():
        dragon_data[id].name = item.name
        dragon_data[id].weight = item.weight
        return dragon_data[id]


if __name__ == "__main__":
    data_base = data_load(data)
    uvicorn.run(app, host="0.0.0.0", port=8000)
