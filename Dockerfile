#FROM python:3-slim
FROM python:2-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
#ENTRYPOINT exec gunicorn -b :$PORT -w 2 main:app
