## Docker Small WebApp

Backend [![Backend Docker Pulls](https://img.shields.io/docker/pulls/renaudhager/backend-training-webapp.svg)](https://hub.docker.com/r/renaudhager/backend-training-webapp)

Frontend [![Frontend Docker Pulls](https://img.shields.io/docker/pulls/renaudhager/frontend-training-webapp.svg)](https://hub.docker.com/r/renaudhager/frontend-training-webapp)

# Description
Small python, inspired by Docker training application. (https://github.com/docker-training/webapp)

## Build
To build this image, run the following command:
```
make build
```

## Run
To run this Docker image, run the following command:
```
docker run -d \
  -p 5000:5000 \
  renaudhager/python-training-webapp:latest
```
