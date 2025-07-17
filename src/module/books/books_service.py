import uuid
from sqlmodel.ext.asyncio.session import AsyncSession
from src.database.model import Book
from src.schemas import BookCreate, BookUpdate , BookResponse
from sqlmodel import select , desc
from src.utils import NotFoundError

class BookService:
    async def get_all_books(self , db: AsyncSession):
      statement = select(Book).order_by(desc(Book.created_at))
      result = await db.exec(statement)
      return result.all()
      
  
    async def get_book_by_id(self , db: AsyncSession , book_id: uuid.UUID):
        statement  = select(Book).where(Book.id == book_id)
        result = await db.exec(statement)
        book = result.first()
        if not book:
            raise NotFoundError("Book not found")
        return BookResponse.model_validate(book)
    
  
    async def create_book(self , db: AsyncSession , book: BookCreate):
        book_data_dict = book.model_dump()
        new_book = Book(**book_data_dict)
        db.add(new_book)
        await db.commit()
        return BookResponse.model_validate(new_book)
       
  
    async def update_book(self , db: AsyncSession , book_id: uuid.UUID , book_update: BookUpdate):
        book_to_update = await self.get_book_by_id(db, book_id)
        if not book_to_update:
            raise NotFoundError("Book not found")
        update_book_data_dict = book_update.model_dump()
        for key, value in update_book_data_dict.items():
            setattr(book_to_update, key, value)
            
        db.add(book_to_update)
        await db.commit()
        await db.refresh(book_to_update)
        return {
            "message": "Book updated successfully",
            "book": BookResponse.model_validate(book_to_update)
        }
    
    async def delete_book(self , db: AsyncSession , book_id: uuid.UUID):
        book_to_delete = await self.get_book_by_id(db, book_id)
        if not book_to_delete:
            raise NotFoundError("Book not found")
        await db.delete(book_to_delete)
        await db.commit()
        return {
            "message": "Book deleted successfully",
            "book": BookResponse.model_validate(book_to_delete)
        }