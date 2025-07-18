import uuid
from sqlmodel import Field, SQLModel
from datetime import datetime

class Book(SQLModel, table=True):
    __table_args__ = {'extend_existing': True}
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(index=True, min_length=1, max_length=255)
    author: str = Field(index=True, min_length=1, max_length=255)
    description: str = Field(index=True, min_length=1, max_length=255)
    price: float = Field(index=True, gt=0)
    quantity: int = Field(index=True, gt=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    def __repr__(self):
        return f"<Book {self.title}>"