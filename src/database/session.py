from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.engine import AsyncSessionLocal

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for FastAPI or other frameworks"""
    async with AsyncSessionLocal() as session:
        yield session