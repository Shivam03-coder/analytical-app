from pydantic import BaseModel
import uuid
from typing import Optional
from datetime import datetime

# Request schemas
class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    price: float
    quantity: int

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

class BookResponse(BaseModel):
    id: uuid.UUID
    title: str
    author: str
    description: str
    price: float
    quantity: int
    created_at: datetime
    
    class Config:
        from_attributes = True 

