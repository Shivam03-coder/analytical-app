from fastapi import APIRouter
from src.module.books import book_router

api_router = APIRouter()

api_router.include_router(book_router, prefix="/books", tags=["Books"])