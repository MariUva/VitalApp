# Imagen base
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias y código
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto de Flask
EXPOSE 8000

# Comando de ejecución
CMD ["python", "app.py"]
