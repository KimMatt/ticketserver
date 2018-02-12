FROM ubuntu:latest
MAINTAINER Matt Kim "mtt.kim@mail.utoronto.ca"
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential python3
COPY . /
WORKDIR /
RUN pip3 install -r requirements.txt
ENV PORT 8000
ENV ENVIRONMENT PROD
EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["server.py"]