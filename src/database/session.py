from src.database.engine import AsyncSessionLocal


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
