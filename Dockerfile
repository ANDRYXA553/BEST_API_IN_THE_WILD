FROM python:3.9-alpine
ENV PYTHONBUFFERED 1
WORKDIR /django
COPY requiremenets.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .