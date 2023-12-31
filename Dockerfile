FROM python:3.11-slim-bullseye

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3", "src/main.py"]