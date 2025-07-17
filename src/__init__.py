# app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.database import init_db, close_db
from src.middleware import ResponseWrapperMiddleware, ErrorWrapper

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("Database initialized")
    yield
    await close_db()
    print("Database closed")

app = FastAPI(title="FastAPI App", version="1.0.0", lifespan=lifespan)

app.add_middleware(ResponseWrapperMiddleware)
ErrorWrapper(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}



# app.include_router(books.router, prefix="/books", tags=["Books"])
