FROM python:3.10-slim
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

<<<<<<<< HEAD:Dockerfile
CMD ["python", ".\black_jack\main.py"]
========
EXPOSE 8888

CMD ["python", "requirements.py"]
>>>>>>>> 6c7ad3a8fa43cce19e06a904f5b62da25dc93d61:black_jack/Dockerfile
