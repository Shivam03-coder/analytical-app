from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlmodel import SQLModel
from src.config import env as settings

async_engine = create_async_engine(
    settings.DATABASE_URL,
    future=True, 
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,  
    autocommit=False,
    autoflush=False,
)

async def init_db():
    """Initialize database tables"""
    async with async_engine.begin() as conn:
        from src.database import Book  
        SQLModel.metadata.clear()
        await conn.run_sync(SQLModel.metadata.create_all)



async def close_db():
    """Close database connections"""
    await async_engine.dispose()