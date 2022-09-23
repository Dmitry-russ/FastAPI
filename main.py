import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from data import data_load


class Item(BaseModel):
    name: str
    weight: int
    description: str
    magic: str
    wingspan: int = None
    max_altitude: int = None
    max_speed: int = None
    strenght: int = None


class Patch_item(BaseModel):
    name: str = None
    weight: int = None
    description: str = None
    magic: str = None
    wingspan: int = None
    max_altitude: int = None
    max_speed: int = None
    strenght: int = None


app = FastAPI()


@app.get("/")
async def get_all():
    return data_base


@app.get("/{someone}/")
async def get_dragon(someone: str):
    if someone not in data_base:
        return {"error": "Class does not exist in data_base"}
    return data_base[someone]


@app.post("/{someone}/")
async def new_dragon(someone: str, item: Item):
    if someone not in classies_keys:
        return {"error": "Class does not exist"}
    someone_new = classies_keys[someone](**item.dict())
    someone_base: dict = data_base[someone]
    count: int = list(someone_base)[-1] if someone_base else 0
    data_base[someone][count+1] = someone_new
    return someone_new


@app.get("/{someone}/{id}")
async def get_one_dragon(someone: str, id: int):
    someone_data: dict = data_base[someone]
    if id not in someone_data.keys():
        return {"error": "id not found"}
    return someone_data[id]


@app.patch("/{someone}/{id}")
async def change_dragon(someone: str, id: int, item: Patch_item):
    if someone not in data_base:
        return {"error": "Class does not exist in data_base"}
    someone_data: dict = data_base[someone]
    if id not in someone_data:
        return {"error": "id not found"}
    make_data = vars(item)
    check_attr = set(dir(someone_data[id]))
    #  надо доделать тут
    for dt in make_data:
        if dt not in check_attr:
            del make_data[dt]
    someone_data[id].patch_metod(vars(item))
    return someone_data[id]


@app.delete("/{someone}/{id}")
async def del_dragon(someone: str, id: int, item: Item):
    if someone not in data_base:
        return {"error": "Class does not exist in data_base"}
    someone_data: dict = data_base[someone]
    if id not in someone_data.keys():
        return {"error": "id not found"}
    del someone_data[id]


if __name__ == "__main__":
    data_base, classies_keys = data_load()
    uvicorn.run(app, host="0.0.0.0", port=8000)
