from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.models.user import User

router = APIRouter()

# Simulando um banco de dados em memória
users_db = []
user_id_counter = 1

@router.get("/", response_model=List[UserResponse])
async def get_users():
    """Retorna todos os usuários"""
    return users_db

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """Retorna um usuário específico pelo ID"""
    user = next((user for user in users_db if user["id"] == user_id), None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    return user

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Cria um novo usuário"""
    global user_id_counter
    
    new_user = {
        "id": user_id_counter,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }
    
    users_db.append(new_user)
    user_id_counter += 1
    
    return new_user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate):
    """Atualiza um usuário existente"""
    user_index = next((i for i, user in enumerate(users_db) if user["id"] == user_id), None)
    
    if user_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    
    # Atualiza apenas os campos fornecidos
    update_data = user_update.dict(exclude_unset=True)
    users_db[user_index].update(update_data)
    
    return users_db[user_index]

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    """Remove um usuário"""
    user_index = next((i for i, user in enumerate(users_db) if user["id"] == user_id), None)
    
    if user_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    
    users_db.pop(user_index)
    return None
