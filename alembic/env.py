import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from alembic import context
from app.core.database import Base
from app.core.config import settings
from app.models.user import User
from app.models.account import Account
from app.models.payment import Payment

from dotenv import load_dotenv
import os

load_dotenv()  # Загружаем переменные окружения

DATABASE_URL = os.getenv("DATABASE_URL")

# Настройка логирования
config = context.config
fileConfig(config.config_file_name)

# alembic.ini 
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Подключаем метаданные моделей
target_metadata = Base.metadata

# Создаём асинхронный движок
def get_engine():
    return create_async_engine(settings.DATABASE_URL, poolclass=pool.NullPool)

async def run_migrations():
    """Асинхронный запуск миграций"""
    connectable = get_engine()
    
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

def do_run_migrations(connection):
    """Запуск миграций"""
    context.configure(connection=connection, target_metadata=target_metadata, render_as_batch=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Запуск Alembic в онлайн-режиме (асинхронно)"""
    asyncio.run(run_migrations())

if context.is_offline_mode():
    context.configure(url=settings.DATABASE_URL, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()
else:
    run_migrations_online()