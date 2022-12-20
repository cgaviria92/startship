# Pull de la imagen base oficial
FROM python:3.9.6


# setup del directorio de trabajo
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app
#COPY . ./code/


EXPOSE 80

#ENTRYPOINT uvicorn app.main:app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

