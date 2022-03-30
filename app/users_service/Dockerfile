FROM python:3.7-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get install -y libmysqlclient-dev && apt-get install -y python-mysqldb && pip install --no-cache-dir -r requirements.txt 
COPY ./users.py .
CMD [ "python", "./users.py" ]