FROM python:3.8.7-slim
COPY requirements.txt /
RUN apt update
RUN apt install default-libmysqlclient-dev build-essential -y
RUN pip3 install -r requirements.txt
COPY . /cookingapp
WORKDIR /cookingapp
EXPOSE 8000
ENTRYPOINT ["sh", "./gunicorn.sh"]