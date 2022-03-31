FROM python:3.7-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential 
RUN pip install --no-cache-dir -r requirements.txt && apt-get install mysql 
RUN pip3 install mysqlclient 
COPY ./users.py .
CMD [ "python", "./users.py" ]