import uuid
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from src.database import Book 
from src.module.books.book_schema import BookCreate, BookUpdate 
from src.utils import NotFoundError

class BookService:
    async def get_all_books(self, db: AsyncSession):
        async with db:
            result = await db.exec(select(Book).order_by(desc(Book)))
            return result.all()
    
    async def get_book_by_id(self, db: AsyncSession, book_id: uuid.UUID):
        async with db:
            book = await db.get(Book, book_id)  
            if not book:
                raise NotFoundError("Book not found")
            return book
    
    async def create_book(self, db: AsyncSession, book: BookCreate):
        async with db:
            new_book = Book(**book.model_dump())
            db.add(new_book)
            await db.commit()
            await db.refresh(new_book)
            return new_book
    
    async def update_book(self, db: AsyncSession, book_id: uuid.UUID, book_update: BookUpdate):
        async with db:
            book = await db.get(Book, book_id)
            if not book:
                raise NotFoundError("Book not found")
            
            update_data = book_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(book, key, value)
            
            db.add(book)
            await db.commit()
            await db.refresh(book)
            return {
                "message": "Book updated successfully",
                "book": book
            }
    
    async def delete_book(self, db: AsyncSession, book_id: uuid.UUID):
        async with db:
            book = await db.get(Book, book_id)
            if not book:
                raise NotFoundError("Book not found")
            
            await db.delete(book)
            await db.commit()
            return {
                "message": "Book deleted successfully",
                "book": book
            }