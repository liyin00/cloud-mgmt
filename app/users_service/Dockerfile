FROM python:3.7-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN chmod +x /sql_connection.sh
RUN /sql_connection.sh
RUN pip install --no-cache-dir -r requirements.txt
COPY ./users.py .
CMD [ "python", "./users.py" ]