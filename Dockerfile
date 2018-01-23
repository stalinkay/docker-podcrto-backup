FROM tozd/cron:ubuntu-xenial

RUN apt-get update -q -q && \
 apt-get --yes --force-yes install python3

COPY ./code /code

COPY ./etc /etc
