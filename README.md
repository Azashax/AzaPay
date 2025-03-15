# 🚀 AzaPay (FastApi) – Инструкция по развертыванию проекта  

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

---

# 🔹 Вариант 1: Запуск с Docker Compose (рекомендуемый)

### 3️⃣ Запуск контейнеров  

#### 🔹 Собрать и запустить контейнеры:  
```bash
docker-compose up --build -d
```
Флаг `-d` запустит контейнеры в фоновом режиме.

#### 🔹 Выполнить миграции базы данных:
```bash
docker-compose exec app alembic upgrade head
```

---

# 🔹 Вариант 2: Запуск без Docker Compose

### 3️⃣ Установка зависимостей  
Убедитесь, что у вас установлены **Python 3**, **PostgreSQL** и **виртуальное окружение**.  

Создайте и активируйте виртуальное окружение:  
```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```

Установите зависимости:  
```bash
pip install -r requirements.txt
```

### 5️⃣ Применение миграций  
```bash
alembic upgrade head
```

### 6️⃣ Запуск приложения  
```bash
python3 main.py
```

# Проверка работы  
После успешного запуска проекта откройте в браузере:

- **API**: `http://localhost:8000`
- **Документация API**: `http://localhost:8000/docs`


# Доступные пользователи  

После выполнения миграций в базе данных уже есть два пользователя:

| Роль  | Email               | Пароль    |
|-------|---------------------|-----------|
| **Администратор** | `admin@example.com` | `admin123` |
| **Обычный пользователь** | `user@example.com`  | `admin123` |

---
