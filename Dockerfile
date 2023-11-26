FROM python:3.11

WORKDIR /app

COPY requirements.txt .

COPY API/ .

RUN pip install -r requirements.txt

EXPOSE 80

ARG mongo_username="admin"

ENV MONGO_USERNAME=$mongo_username

ARG mongo_password

ENV MONGO_PASSWORD=$mongo_password

ENTRYPOINT [ "python", "app.py" ]
