FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8084

CMD ["gunicorn", "-b", "0.0.0.0:8083", "app:app"]
