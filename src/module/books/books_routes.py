import uuid
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.database.session import get_session
from src.module.books.books_service import BookService
from src.module.books.book_schema import  BookCreate, BookUpdate ,BookResponse 
from typing import Sequence

book_router = APIRouter()
book_service = BookService()

@book_router.get("/", response_model=Sequence[BookResponse])
async def get_all_books(db: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(db)
    return books

@book_router.get("/{book_id}", response_model=BookResponse)
async def get_book_by_id(book_id: uuid.UUID, db: AsyncSession = Depends(get_session)):
    return await book_service.get_book_by_id(db, book_id)

@book_router.post("/", response_model=BookResponse)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_session)):
    return await book_service.create_book(db, book)

@book_router.put("/{book_id}", response_model=BookResponse)
async def update_book(book_id: uuid.UUID, book: BookUpdate, db: AsyncSession = Depends(get_session)):
    return await book_service.update_book(db, book_id, book)

@book_router.delete("/{book_id}", response_model=BookResponse)
async def delete_book(book_id: uuid.UUID, db: AsyncSession = Depends(get_session)):
    return await book_service.delete_book(db, book_id)
