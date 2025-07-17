from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlmodel import SQLModel
from src.config import  env as settings
from src.database.model import Book

async_engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
    future=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def init_db() -> None:
    async with async_engine.begin() as conn:
        from src.database.model import Book
        await conn.run_sync(SQLModel.metadata.create_all)

async def close_db() -> None:
    await async_engine.dispose()


