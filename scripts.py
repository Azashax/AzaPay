import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.database import get_db
from app.models.user import User
from app.models.account import Account

async def create_fake_users(db: AsyncSession):
    """Создаёт фейковых пользователей, включая администратора"""

    # Проверяем, есть ли уже пользователи
    result = await db.execute(select(User))
    if result.scalars().first():
        print("❌ Пользователи уже существуют. Пропускаем создание.")
        return

    # Создаём админа
    admin = User(
        email="admin@example.com",
        first_name="Admin",
        last_name="User",
        is_admin=True
    )
    
    admin.set_password("admin123")
    
    # Создаём обычного пользователя
    user = User(
        email="user@example.com",
        first_name="John",
        last_name="Doe",
        is_admin=False
    )
    
    user.set_password("admin123")
    
    db.add_all([admin, user])
    await db.commit()
    print("✅ Фейковые пользователи добавлены!")

async def create_fake_accounts(db: AsyncSession):
    """Создаёт фейковые аккаунты"""
    users = await db.execute(select(User))
    users = users.scalars().all()

    if not users:
        print("❌ Нет пользователей для создания аккаунтов!")
        return

    accounts = [Account(user_id=user.id, balance=1000.0) for user in users]
    db.add_all(accounts)
    await db.commit()
    print("✅ Фейковые аккаунты добавлены!")

async def main():
    """Основная функция для создания фейковых данных"""
    async for db in get_db():  # ✅ Используем `async for`, чтобы получить сессию
        await create_fake_users(db)
        await create_fake_accounts(db)

if __name__ == "__main__":
    asyncio.run(main())  # ✅ Теперь код работает правильно!
