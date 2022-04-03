FROM ubuntu:latest
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get update && apt-get install python3-pip 
RUN python3-pip install --no-cache-dir -r requirements.txt
COPY ./elegant-fort-344208-514b10873dd0.json .
COPY ./product.py .
CMD [ "python3", "./product.py" ]
