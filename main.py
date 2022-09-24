import uvicorn
from fastapi import FastAPI, Body


from data import data_load

app = FastAPI()


@app.get("/")
async def get_all():
    return data_base


@app.get("/{someone}/")
async def get_dragon(someone: str):
    if someone not in data_base:
        return {"error": "Class does not exist in data_base"}
    return data_base[someone]


@app.get("/{someone}/{id}")
async def get_one_dragon(someone: str, id: int):
    someone_data: dict = data_base[someone]
    if id not in someone_data.keys():
        return {"error": "id not found"}
    return someone_data[id]


@app.post("/{someone}/")
async def new_someone(someone: str, item: dict = Body()):
    if someone not in classies_keys:
        return {"error": "Class does not exist"}
    try:
        someone_new = classies_keys[someone](**item)
    except TypeError:
        return {"error": "Not such attr. Check your data."}
    count: int = list(data_base[someone])[-1] if data_base[someone] else 0
    data_base[someone][count+1] = someone_new
    return someone_new


@app.patch("/{someone}/{id}")
async def change_someone(someone: str, id: int, item: dict = Body()):
    if someone not in data_base:
        return {"error": "Class does not exist in data_base."}
    someone_data: dict = data_base[someone]
    if id not in someone_data:
        return {"error": "id not found."}
    for key in item:
        if key in dir(someone_data[id]):
            setattr(someone_data[id], key, item[key])
    return someone_data[id]


@app.delete("/{someone}/{id}")
async def del_someone(someone: str, id: int):
    if someone not in data_base:
        return {"error": "Class does not exist in data_base"}
    someone_data: dict = data_base[someone]
    if id not in someone_data.keys():
        return {"error": "id not found"}
    del someone_data[id]


if __name__ == "__main__":
    data_base, classies_keys = data_load()
    uvicorn.run(app, host="0.0.0.0", port=8000)
