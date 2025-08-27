from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    """Schema base para usuários"""
    name: str = Field(..., min_length=1, max_length=100, description="Nome do usuário")
    email: EmailStr = Field(..., description="Email do usuário")
    age: Optional[int] = Field(None, ge=0, le=150, description="Idade do usuário")

class UserCreate(UserBase):
    """Schema para criação de usuário"""
    pass

class UserUpdate(BaseModel):
    """Schema para atualização de usuário"""
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="Nome do usuário")
    email: Optional[EmailStr] = Field(None, description="Email do usuário")
    age: Optional[int] = Field(None, ge=0, le=150, description="Idade do usuário")

class UserResponse(UserBase):
    """Schema para resposta de usuário"""
    id: int = Field(..., description="ID único do usuário")
    
    class Config:
        from_attributes = True