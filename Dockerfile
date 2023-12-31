FROM python:3.10-slim
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "./black_jack/main.py"]

