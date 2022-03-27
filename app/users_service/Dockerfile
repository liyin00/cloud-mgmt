FROM python:3.7-slim
ARG SA_KEY
ENV SA_KEY = ${{ secrets.GKE_SA_KEY }}
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./users.py .
CMD [ "python", "./users.py" ]
