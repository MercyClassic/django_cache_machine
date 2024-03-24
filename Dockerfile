FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTEDECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/src

COPY ./pyproject.toml /app/pyproject.toml

RUN apt update \
    && pip install poetry \
    && apt install -y libmagic1 \
    && chdir /app \
    && poetry config virtualenvs.create false \
    && poetry install --only main

WORKDIR /app/src

COPY . /app

EXPOSE 8000

CMD ["sh", "/app/entrypoint.sh"]
