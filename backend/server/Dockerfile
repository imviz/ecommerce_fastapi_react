FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# COPY requirements.txt ./requirements.txt
# RUN pip install --upgrade pip
# RUN pip install -r ./requirements.txt

# COPY app ./app

# WORKDIR /app/
# ENV PYTHONPATH=/app


# COPY requirements.txt /app/requirements.txt
COPY ./server/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
# COPY ./server/prestart.sh /app/prestart.sh
# COPY ./server/alembic.ini /app/alembic.ini
# COPY ./server/config.yml /app/config.yml

COPY ./server/alembic /app/alembic
COPY ./server/app /app/app
WORKDIR /app/

ENV PYTHONPATH=/app

# EXPOSE 80
