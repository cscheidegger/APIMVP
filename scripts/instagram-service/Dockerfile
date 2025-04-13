
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY instagram_feed.py /app/

CMD ["python", "instagram_feed.py"]
