FROM ubuntu:latest
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get install python-pip && python-pip install --no-cache-dir -r requirements.txt
COPY ./elegant-fort-344208-514b10873dd0.json .
COPY ./product.py .
CMD [ "python", "./product.py" ]
