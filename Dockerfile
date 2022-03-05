FROM python:3.7.2-alpine3.8
LABEL maintainer="Alphaalex"
EXPOSE 8000
RUN apk update && apk upgrade && apk add bash
RUN apk --update add postgresql-dev gcc python3-dev musl-dev
RUN apk add zlib-dev jpeg-dev gcc musl-dev
COPY . .
RUN ["pip", "install", "-r", "requirements.txt"]