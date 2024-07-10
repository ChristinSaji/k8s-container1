FROM python:3.9-slim

WORKDIR /app

COPY app1.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD ["python", "app1.py"]
