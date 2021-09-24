FROM python:3.9-alpine
ENV PYTHONBUFFERED 1
WORKDIR /BEST_API_IN_THE_WILD
COPY requiremenets.txt requirements.txt
RUN apk add build-base jpeg-dev zlib-dev libffi-dev
RUN pip3 install -r requirements.txt
COPY . .