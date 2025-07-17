import uuid
from sqlmodel import Field, SQLModel, create_engine, select, table
from datetime import datetime

class Book(SQLModel , table=True):
    id: uuid.UUID = Field(default=uuid.uuid4(), primary_key=True)
    title: str = Field(index=True, min_length=1, max_length=255)
    author: str = Field(index=True, min_length=1, max_length=255)
    description: str = Field(index=True, min_length=1, max_length=255)
    price: float = Field(index=True, gt=0)
    quantity: int = Field(index=True, gt=0)
    created_at: datetime = Field(index=True, default=datetime.now())

    class Config:
        table_name = "books"
        
    def __repr__(self):
        return f"<Book {self.title}>"
    