from fastapi import APIRouter, HTTPException, status, Request
from typing import List
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate

router = APIRouter()

@router.post("/")
async def respond_recieved_message(request: Request):
    body = await request.json()
    print(body)
    return {"message": "Message received"}