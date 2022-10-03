import uvicorn
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse

from data import (data_load,
                  post_examples,
                  patch_examples, get_responses,
                  get_class_response, get_id_response,
                  del_response, post_response, patch_response)

data_base, classies_keys = data_load()

app = FastAPI()


@app.get("/", responses=get_responses)
async def get_all():
    return data_base

# http://127.0.0.1:8000/creatures/?creature_kind=dragon
@app.get("/creatures/", responses=get_responses)
async def get_with_params(creature_kind: str = ""):
    return f"You want a creature {creature_kind}"

# тут все будет ОК, т.к. этот url выше
@app.get("/another_url/", responses=get_responses)
async def get_another_url():
    return "Show results for another_url"


@app.get("/{someone}/", status_code=200, responses=get_class_response)
async def get_someone(someone: str):
    if someone not in data_base:
        return JSONResponse(
            content={"error": "Class does not exist in data_base"},
            status_code=400)
    return data_base[someone]

# а вот сюда мы не будем попадать
@app.get("/another_url_2/", responses=get_responses)
async def get_another_url_2():
    return "Show results for another_url_2"


@app.get("/{someone}/{id}", responses=get_id_response)
async def get_someone_id(someone: str, id: int):
    someone_data: dict = data_base[someone]
    if id not in someone_data.keys():
        return JSONResponse(content={"error": "id not found"}, status_code=400)
    return someone_data[id]


@app.post("/{someone}/", status_code=201, responses=post_response)
async def new_someone(someone: str, item: dict = Body(examples=post_examples)):
    if someone not in classies_keys:
        return JSONResponse(
            content={"error": "Class does not exist"}, status_code=400)
    try:
        someone_new = classies_keys[someone](**item)
    except TypeError:
        return JSONResponse(
            content={
                "error": "Not such attr. in this class. Check your data."},
            status_code=406)
    count: int = list(data_base[someone])[-1] + 1 if data_base[someone] else 0
    data_base[someone][count] = someone_new
    return {"created": {count: someone_new}}


@app.patch("/{someone}/{id}", responses=patch_response)
async def change_someone(
        someone: str, id: int, item: dict = Body(examples=patch_examples)):
    if someone not in data_base:
        return JSONResponse(
            content={"error": "Class does not exist in data_base."},
            status_code=400)
    someone_data: dict = data_base[someone]
    if id not in someone_data:
        return JSONResponse(
            content={"error": "id not found."}, status_code=400)
    for key in item:
        if key in dir(someone_data[id]):
            setattr(someone_data[id], key, item[key])
    return {"changed": {id: someone_data[id]}}


@app.delete("/{someone}/{id}", responses=del_response)
async def del_someone(someone: str, id: int):
    if someone not in data_base:
        return {"error": "Class does not exist in data_base"}
    someone_data: dict = data_base[someone]
    if id not in someone_data.keys():
        return {"error": "id not found"}
    del someone_data[id]
    return f'Deleted: type {someone}, id {id}'


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
