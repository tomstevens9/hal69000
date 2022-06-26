FROM debian:bookworm
RUN apt-get update && apt-get install -y python3 python3-pip postgresql-client

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip install -r requirements.txt

CMD ["/bin/bash", "./start.sh"]
