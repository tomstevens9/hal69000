FROM debian:bookworm

SHELL ["/bin/bash", "--login", "-c"]

RUN apt-get update && apt-get install -y python3 python3-pip postgresql-client curl

# Install Node
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
RUN nvm install --lts

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD package.json /app/
RUN npm install

ADD . /app/

RUN npm run build
CMD ["/bin/bash", "./start.sh"]
