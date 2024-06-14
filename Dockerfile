FROM python:3.9-alpine

# Crear directorio de trabajo
WORKDIR /app

# Copiar y instalar las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . /app

# Definir un volumen para persistir datos
VOLUME /app/data

# Configurar variables de entorno
ENV PORT=8000

# Exponer el puerto de la aplicación
EXPOSE $PORT

# Comando para ejecutar Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]

