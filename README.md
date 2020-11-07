# Dockerized ML

Repo to exemplify dockerization of ML models. 

Key points:

1. Build your Docker image by typing in from main folder: `docker build -t basic_clf:1.0 . ` This will create 
an image named `basic_clf` with tag `1.0`

2. Upon successful image built, confirm your image has indeed been created by typing in `docker images`. Information
about your image should be displayed. 

3. To run the docker image just created, type in `docker run --name deployedCLF -p 8080:8080 basic_clf:1.0`. 
Here *deployedCLF* will be the name of the container.

4. Upon execution of the command above you can check your docker container is running by typing in `docker ps` 

**Important**. The main goal of this repo is to exemplify the process of dockerizing the ML algorithm. Thus, the model
deployed may not be sound in terms of performance - it will be refined as this repo is maintained

