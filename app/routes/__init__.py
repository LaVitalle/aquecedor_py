from fastapi import APIRouter
from .users import router as users_router
from .items import router as items_router
from .whatsapp import router as whatsapp_router

api_router = APIRouter()

# Incluindo as rotas dos diferentes módulos
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(items_router, prefix="/items", tags=["items"])
api_router.include_router(whatsapp_router, prefix="/whatsapp", tags=["whatsapp"])
