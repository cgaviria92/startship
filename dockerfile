# Pull de la imagen base oficial
FROM python:3.9.6

# setup del directorio de trabajo
WORKDIR /code

# Copiar archivos de código y requerimientos
COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app
COPY ./init.sql /docker-entrypoint-initdb.d/

# Instalar dependencias
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Exponer el puerto 80
EXPOSE 80

# Iniciar la aplicación FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
