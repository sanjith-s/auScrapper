from fastapi import FastAPI
from run import scrapData
import json

app = FastAPI()


#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/getNews")
async def get_News():
    resList = scrapData()
    return {"newsData": json.dumps(resList)}
