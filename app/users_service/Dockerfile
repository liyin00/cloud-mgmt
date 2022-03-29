FROM python:3.7-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY ../.env ./
RUN pip install --no-cache-dir -r requirements.txt

# RUN --mount=type=secret,id=PASSWORD \
#   --mount=type=secret,id=PUBLIC_IP_ADDRESS \
#   --mount=type=secret,id=DBNAME \
#   --mount=type=secret,id=PROJECT_ID \
#   --mount=type=secret,id=INSTANCE_NAME \ 
#   --mount=type=secret,id=SA_KEY \ 
#   export PASSWORD=$(cat /run/secrets/PASSWORD) && \
#   export PUBLIC_IP_ADDRESS=$(cat /run/secrets/PUBLIC_IP_ADDRESS) && \
#   export DBNAME=$(cat /run/secrets/DBNAME) && \
#   export PROJECT_ID=$(cat /run/secrets/PROJECT_ID) && \
#   export INSTANCE_NAME=$(cat /run/secrets/INSTANCE_NAME)
COPY ./users.py .
CMD [ "python", "./users.py" ]