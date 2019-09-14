FROM alpine

# prep
ENV PYTHONUNBUFFERED 1
ENV PYTHONASYNCIODEBUG 1
ENV PYTHONDONTWRITEBYTECODE 1


# init
RUN mkdir /app
WORKDIR /app


# setup
RUN apk update \
    && apk upgrade \
    && apk --no-cache add \
    bash \
    python3 \
    python3-dev \
    postgresql-client \
    postgresql-dev \
    build-base \
    gettext \
    jpeg-dev \
    zlib-dev \
    graphviz \
    graphviz-dev \
    ttf-freefont \
    openssh-client



ADD . /app/
RUN python3 -m pip install -U pip && python3 -m pip install -r requirements.txt

RUN chmod 777 logs/

# Run bash script for waiting for db
COPY scripts/wait-for-postgres.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-postgres.sh
