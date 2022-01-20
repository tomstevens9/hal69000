FROM debian:bookworm
RUN apt-get update && apt-get install -y python3 python3-pip
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY discord_bot .
CMD ["gunicorn", "main.wsgi:application", "--bind", "0.0.0.0:8080"]
