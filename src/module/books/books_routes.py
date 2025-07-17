from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.database.session import get_db
from src.module.books import BookService, BookCreate, BookUpdate, BookResponse

book_router = APIRouter()

@book_router.get("/books")
async def get_all_books(db: AsyncSession = Depends(get_db)):
    books = await BookService().get_all_books(db)
    return books


