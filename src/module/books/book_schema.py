import uuid
from pydantic import BaseModel
from datetime import datetime

class BookCreate(BaseModel):
     title: str
     author: str
     description: str
     price: float
     quantity: int

class BookUpdate(BaseModel):
     title: str
     author: str
     description: str
     price: float
     quantity: int
 
class BookResponse(BaseModel):
     id: uuid.UUID
     title: str
     author: str
     description: str
     price: float
     quantity: int
     created_at: datetime
































