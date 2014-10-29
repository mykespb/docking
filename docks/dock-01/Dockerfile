FROM ubuntu:14.04
MAINTAINER Mikhail Kolodin <mykespb@gmail.com>

RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y python-pip python-dev && apt-get clean

RUN pip install bottle
#RUN pip install gunicorn

EXPOSE 8080

ADD . /app
WORKDIR /app

#RUN chown -R apprunner:apprunner /app
#USER apprunner

#RUN groupadd -r apprunner
#RUN useradd -r -g apprunner -d / -s /usr/sbin/nologin -c "Docker image user" apprunner

CMD ["python", "/app/main.py"]

