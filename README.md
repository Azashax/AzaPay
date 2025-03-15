# 🚀 AzaPay – Инструкция по развертыванию проекта

## 1️⃣ Клонирование репозитория  
Откройте терминал и выполните команду:  
```bash
git clone <URL_РЕПОЗИТОРИЯ>
cd <ИМЯ_ПРОЕКТА>
```

## 2️⃣ Создание `.env` файла  
В корневой папке создайте файл **`.env`** и добавьте в него следующие переменные окружения:  

```env
DATABASE_URL=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
REFRESH_TOKEN_EXPIRE_DAYS=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
```
Заполните значения в соответствии с вашей конфигурацией.

## 3️⃣ Запуск проекта с Docker  

### 🔹 Собрать и запустить контейнеры:  
```bash
docker-compose up --build -d
```
Флаг `-d` запустит контейнеры в фоновом режиме.

### 🔹 Выполнить миграции базы данных:
```bash
docker-compose exec app alembic upgrade head
```

### 🔹 (Опционально) Создать суперпользователя (если требуется):  
```bash
docker-compose exec app python manage.py createsuperuser
```
Введите email и пароль для администратора.

## 4️⃣ Проверка работы  
После успешного запуска проекта откройте в браузере:

- **API**: `http://localhost:8000`
- **Документация API (если используется FastAPI)**: `http://localhost:8000/docs`

✅ Готово! Теперь ваш проект **AzaPay** развернут и работает. 🚀
