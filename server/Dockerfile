FROM python:3.9.10-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update

RUN apt-get -y install default-libmysqlclient-dev gcc

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]