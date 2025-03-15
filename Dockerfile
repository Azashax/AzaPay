# Используем Python 3.11
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Открываем порт
EXPOSE 8000

# Указываем команду для запуска
CMD ["sh", "-c", "python /app/scripts.py && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]