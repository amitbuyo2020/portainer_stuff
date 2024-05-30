FROM python:3.9-slim

WORKDIR /app

COPY . /app/

RUN pip install -r no-cache-dir requirements.txt

CMD [ "python", "main.py"]





