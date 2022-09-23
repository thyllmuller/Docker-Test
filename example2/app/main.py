from typing import Union
from fastapi import FastAPI

app = FastAPI()  # Here the app variable will be an "instance" of the class FastAPI.


# lots of overarching FAPI info here: https://fastapi.tiangolo.com/tutorial/first-steps/
@app.get("/")  # fast api -> GET: to read data.
@app.get("/home")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    secondary_info: Union[str | None] = f"This is item: {item_id}"  # testing 3.10 changes to union
    return {"item_id": item_id, "secondary_info": secondary_info}
