from fastapi import APIRouter, HTTPException, status, Request
from typing import List
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
import requests

router = APIRouter()


@router.post("/")
async def respond_recieved_message(request: Request):
    body = await request.json()
    instance = body["instance"]
    data = body["data"]
    message = data["message"]
    conversation = message["conversation"]
    sender = data["sender"]
    server_url = data["server_url"]
    apikey = data["apikey"]

    # Send message to whatsapp
    url = f"{server_url}/message/sendText/{instance}"
    headers = {"Content-Type": "application/json", "apikey": apikey}
    data = {
        "number": sender,
        "options": {
            "delay": 123,
            "presence": "composing",
            "linkPreview": True,
            "quoted": {
                "key": {
                    "remoteJid": sender,
                    "fromMe": True,
                    "id": message["id"],
                    "participant": sender
                },
                "message": {
                    "conversation": conversation
                }
            },
        },
        "textMessage": {
            "text": "Olá, estou enviando uma mensagem de teste"
        }
    }
    if data['key']['fromMe']:
        response = requests.post(url, headers=headers, json=data)
        print(response.json())
    else:
        print("Message is not from me")
    return {"message": "Message sent"}

# {'event': 'messages.upsert', 'instance': 'Vitor', 'data': {'key': {'remoteJid': '120363402492422239@g.us', 'fromMe': False, 'id': 'AC7BDE53C272D5D1C64924DAFCA5BD35', 'participant': '555193100477@s.whatsapp.net', 'participantLid': '196091127541894@lid'}, 'pushName': 'Xavier', 'status': 'DELIVERY_ACK', 'message': {'messageContextInfo': {'messageSecret': '3p9/BzkVl/inM/MYgf0ke/UEAeb3M12Yt8ms6VbS37s='}, 'conversation': 'Estagiário Engenharia de Dados | 100% Remoto | SPC Brasil \n\n🪧Apenas compartilhando, mais informações somente no link da vaga.\n\nRequisitos: \n\n- Que esteja cursando o Ensino Superior na área de Dados/Tecnologia ou Desenvolvimento a partir do 2º semestre de curso e que tenha pelo menos um ano ainda para finalizá-lo; \n- Disponibilidade para atuar numa jornada de 6 horas diárias no\nperíodo comercial;\n- Aceitamos candidaturas de todos os estados do Brasil pois as vagas são 100% remotas. \n\nO que oferecemos:\n\n- Vaga 100% remota;\n- Auxílio Home Office;\n- Bônus anual;\n- Vale Refeição e Alimentação;\n- Plano de Saúde e Odontológico Sulamerica;\n- Seguro de vida;\n- Day off no seu aniversário;\n- Médico do Trabalho;\n- Consultoria jurídica;\n- Parcerias Educacionais, entre outros.\n\nLink da vaga: https://lnkd.in/d7mtjzGN'}, 'contextInfo': {'forwardingScore': 1, 'isForwarded': True}, 'messageType': 'conversation', 'messageTimestamp': 1756318511, 'instanceId': '3bff8a22-8a3c-40e0-8bf0-d50b4210c520', 'source': 'android'}, 'destination': 'https://dados-aquecedor-py.ekguof.easypanel.host/api/whatsapp', 'date_time': '2025-08-27T15:15:11.329Z', 'sender': '554598231771@s.whatsapp.net', 'server_url': 'https://apiwhatsapp-evolution-api.ekguof.easypanel.host', 'apikey': '1001A3F6CAD4-4B20-B22B-01359394E6C9'}
# curl --request POST \
#  --url https://{server-url}/message/sendText/{instance} \
#  --header 'Content-Type: application/json' \
#  --header 'apikey: <api-key>' \
# --data '{
# "number": "<string>",
# "options": {
#   "delay": 123,
#   "presence": "composing",
#   "linkPreview": true,
#   "quoted": {
#     "key": {
#       "remoteJid": "<string>",
#       "fromMe": true,
#       "id": "<string>",
#       "participant": "<string>"
#     },
#     "message": {
#       "conversation": "<string>"
#     }
#   },
#   "mentions": {
#     "everyOne": true,
#     "mentioned": [
#       "<string>"
#     ]
#   }
# },
# "textMessage": {
#   "text": "<string>"
# }
#}'
