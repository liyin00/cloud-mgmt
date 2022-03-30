FROM ubuntu:latest
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get install -y default-libmysqlclient-dev python-pip python-mysqldb 
RUN pip install --no-cache-dir -r requirements.txt 
COPY ./users.py .
CMD [ "python", "./users.py" ]