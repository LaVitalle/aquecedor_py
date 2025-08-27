from fastapi import APIRouter, HTTPException, status, Request
from typing import List
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
import requests

router = APIRouter()


@router.post("/")
async def respond_recieved_message(request: Request):
    body = await request.json()
    print(body)
    print(
        "--------------------------------------------------------------------------------------------------------------------------------------------------------"
    )
    instance_id = body["data"]["instanceId"]
    server_url = body["server_url"]
    apikey = body["apikey"]
    message = body["data"]["message"]["conversation"]

    # Send message to whatsapp
    url = f"{server_url}/message/sendText/{instance_id}"
    headers = {"Content-Type": "application/json", "apikey": apikey}
    data = {
        "number": "5545998231771@s.whatsapp.net",
        "options": {
            "key": {
                "remoteJid": "5545998231771@s.whatsapp.net",
            }
        },
        "textMessage": {"text": f"Olá! Mensagem recebida com sucesso. {message}"},
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    return {"message": "Message sent"}
