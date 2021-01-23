# This project consists of 2 docker containers
1. Rest API to the different ifcJSON project tools
2. Web app that provides a user interface to these tools, more information: https://github.com/IFCJSON-Team/ifcJSON_docker/blob/master/readme.pdf

# Using the rest API
## Build

Build container using docker file

```docker build -f ./docker/Dockerfile -t ifcjson/ifcjson-api:0.0.1 -t ifcjson/ifcjson-api:latest .```

## Run
example run command with a shell so you can use the container as an isolated env

```docker run --rm -ti -d -p 3200:3200 --name=ifcjson-api ifcjson/ifcjson-api:latest```