from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate

router = APIRouter()

# Simulando um banco de dados em memória
items_db = []
item_id_counter = 1

@router.get("/", response_model=List[ItemResponse])
async def get_items():
    """Retorna todos os itens"""
    return items_db

@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    """Retorna um item específico pelo ID"""
    item = next((item for item in items_db if item["id"] == item_id), None)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado"
        )
    return item

@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """Cria um novo item"""
    global item_id_counter
    
    new_item = {
        "id": item_id_counter,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "available": item.available
    }
    
    items_db.append(new_item)
    item_id_counter += 1
    
    return new_item

@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item_update: ItemUpdate):
    """Atualiza um item existente"""
    item_index = next((i for i, item in enumerate(items_db) if item["id"] == item_id), None)
    
    if item_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado"
        )
    
    # Atualiza apenas os campos fornecidos
    update_data = item_update.dict(exclude_unset=True)
    items_db[item_index].update(update_data)
    
    return items_db[item_index]

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    """Remove um item"""
    item_index = next((i for i, item in enumerate(items_db) if item["id"] == item_id), None)
    
    if item_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado"
        )
    
    items_db.pop(item_index)
    return None
