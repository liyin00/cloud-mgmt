FROM ubuntu:latest
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get update -y && apt-get install -y python3-pip 
RUN pip install --no-cache-dir -r requirements.txt
COPY ./elegant-fort-344208-514b10873dd0.json .
COPY ./product.py .
CMD [ "python3", "./product.py" ]
