import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.main import app
from app.core.db_async import Base
from app.core.deps import get_db


TEST_DATABASE_URL = ("sqlite+aiosqlite:///./test.db")

engine = create_async_engine(TEST_DATABASE_URL)

TestingSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

@pytest_asyncio.fixture(scope="session")
async def setup_database():

    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )

    yield

    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.drop_all
        )

@pytest_asyncio.fixture
async def db():
    async with TestingSessionLocal() as session:
        yield session

async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[
    get_db
] = override_get_db

@pytest_asyncio.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac