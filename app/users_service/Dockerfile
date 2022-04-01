FROM python:3.7-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get update && apt-get install -y && apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip install --no-cache-dir -r requirements.txt 
COPY ./users.py .
CMD [ "python", "./users.py" ]