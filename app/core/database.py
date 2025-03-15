from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# ✅ Создаём асинхронный движок (engine)
engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

# ✅ Создаём фабрику сессий (sessionmaker) для асинхронной работы
async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# ✅ Создаём базовый класс моделей
Base = declarative_base()

# ✅ Функция для получения асинхронной сессии
async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
