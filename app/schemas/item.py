from pydantic import BaseModel, Field
from typing import Optional

class ItemBase(BaseModel):
    """Schema base para itens"""
    name: str = Field(..., min_length=1, max_length=100, description="Nome do item")
    description: Optional[str] = Field(None, max_length=500, description="Descrição do item")
    price: float = Field(..., ge=0, description="Preço do item")
    available: bool = Field(True, description="Se o item está disponível")

class ItemCreate(ItemBase):
    """Schema para criação de item"""
    pass

class ItemUpdate(BaseModel):
    """Schema para atualização de item"""
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="Nome do item")
    description: Optional[str] = Field(None, max_length=500, description="Descrição do item")
    price: Optional[float] = Field(None, ge=0, description="Preço do item")
    available: Optional[bool] = Field(None, description="Se o item está disponível")

class ItemResponse(ItemBase):
    """Schema para resposta de item"""
    id: int = Field(..., description="ID único do item")
    
    class Config:
        from_attributes = True
