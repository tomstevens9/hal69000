FROM debian:bookworm
RUN apt-get update && apt-get install -y python3 python3-pip libopus-dev ffmpeg
RUN mkdir /app
RUN mkdir /app/sounds
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
CMD ["python3", "main.py"]
