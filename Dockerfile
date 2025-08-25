FROM python:3.12.3-slim

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8000
