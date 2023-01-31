from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from run import scrapData
import json

from models import Data

router = APIRouter()


@router.post("/", response_description="Insert Data", status_code=status.HTTP_201_CREATED, response_model=Data)
def create_book(request: Request, data: Data = Body(...)):
    dataStr = json.dumps(scrapData())
    new_data = request.app.database["data"].insert_one(dataStr)
    created_data = request.app.database["data"].find_one(
        {"_id": new_data.inserted_id}
    )

    return created_data


@router.get("/", response_description="List all data", response_model=List[Data])
def list_books(request: Request):
    data = list(request.app.database["data"].find(limit=100))
    return data
