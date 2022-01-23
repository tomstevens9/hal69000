FROM debian:bookworm
RUN apt-get update && apt-get install -y python3 python3-pip postgresql-client
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY discord_bot .
RUN mkdir /app/staticfiles
RUN mkdir /app/media
COPY start.sh .
CMD ["/bin/bash", "./start.sh"]
