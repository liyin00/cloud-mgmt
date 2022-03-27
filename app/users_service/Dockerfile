FROM python:3.7-slim
ARG SA_KEY
ARG PASSWORD
ARG PUBLIC_IP_ADDRESS
ARG DBNAME 
ARG PROJECT_ID
ENV SA_KEY = ${{secrets.GKE_SA_KEY}}
ENV PASSWORD = ${{secrets.GKE_SQL_USER_PW}}
ENV DBNAME = ${{secrets.GKE_SQL_NAME}}
ENV PROJECT_ID = ${{secrets.GKE_PROJECT}}
ENV PUBLIC_IP_ADDRESS = 34.142.229.136
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./users.py .
CMD [ "python", "./users.py" ]

