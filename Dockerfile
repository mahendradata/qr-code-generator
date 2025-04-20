FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:6000", "app:app"]
