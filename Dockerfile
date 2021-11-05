FROM python:3.7.2-alpine3.8
LABEL maintainer="Alphaalex"
EXPOSE 8000
RUN apk update && apk upgrade && apk add bash
COPY . .
RUN ["pip", "install", "-r", "requirements.txt"]
CMD ["python","manage.py","runserver","0.0.0.0:8000","--insecure"]