from fastapi import APIRouter, HTTPException, status, Request
from typing import List
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate

router = APIRouter()

@router.post("/")
async def respond_recieved_message(HttpReq: Request):
    print(HttpReq)
    return {"message": "Message received"}