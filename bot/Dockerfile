FROM debian:bookworm
RUN apt-get update && apt-get install -y python3 python3-pip
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD ["python", "main.py"]
