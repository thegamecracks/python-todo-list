import os

from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from .models import Base

app = FastAPI()
engine = create_async_engine(
    "postgresql+asyncpg://{user}:{password}@{host}:{port}/{dbname}".format(
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host="db",  # service name defined in docker-compose.yml
        port=5432,
        dbname=os.environ["POSTGRES_DB"],
    )
)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def on_shutdown():
    await engine.dispose()


@app.get("/")
async def index():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 'Hello world!'"))
        return {"message": result.scalar_one()}
