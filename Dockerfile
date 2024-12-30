FROM python:3.8-slim-buster 
# it is basically a lighter version / Base image

WORKDIR /app 
# working directory for this perticular container

COPY . /app
# data inside the local system will copy & put insde app folder

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
# command