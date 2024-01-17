FROM python:3.11-slim-bullseye

WORKDIR /opt/app

ENV TZ 'UTC+3' 
ENV PYTHONUNBUFFERED=1

RUN apt update \
    && apt install -y gcc bash \
    && pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python" , "main.py"  ]