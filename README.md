# Docker 
This Repository contains information about docker and its usage. It also contains small projects based on computer-vision and docker. 

Download and Install Docker-Desktop from "https://www.docker.com/products/docker-desktop/"

## Why docker?
Docker can be used to wrap-up an application  which is encapsulated, isolated and portable. The docker containers start instantly. They have their own built-in mechanism for versioning and reuse of components. It can be shared easily using public **Docker Hub** or private repository. 

## Usage

To dockerize any application, create a folder with the application. For example, consider using a folder ./src with a application main.py. 

#### Create a dockerfile

Docker can build images automatically by reading the instructions from the Dockerfile. The **Dockerfile** contains all the commands that are necessary to build an image.It is always named as "Dockerfile".
1. The docker file must always begin with a **FROM** instruction. **FROM** defines a base image which can be pulled from docker hub. For example, if we want to create a python application, then we need to have python as the base image, so it can run python application.

2. **RUN** command is used to run specified commands. One can use several run commands to execute multiple commands. But the most efficient way is to use a single RUN command which contains multiple commands seperated by **&&**.

3. To run a docker container using specific command, **CMD** is used. Specifying more than one CMD command will allow only the last one to get executed. 

4. **WORKDIR** instruction specifies the working directory of that container. Any command that is executed after WORKDIR will be executed within this working directory.

5. **COPY** instruction is used to copy a complete directory or file from the local machine to the docker container. 

## Containerize an Application

1. Build container Image - **docker build -t MyFirstImage .** 
    "MyFirstImage" is the name of the image we are going to build. The '.' at the end of the command tells the docker that it should look for the Docker file in the current Directory. 
2. Start a container(For the first time) - **docker run MyFirstImage**
3. List the containers - **docker ps**
4. On creating a container, it is created with random names. To rename the container - **docker rename "old-container-name" "new-container-name"**
5. To stop a container - **docker stop "container-name"**
6. To start a container - **docker start "container-name"**
7. Remove a docker container - **docker rm MyFirstImage**
