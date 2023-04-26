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

2. **RUN** command is used to run specified commands. One can use several run commands to execute multiple commands. But the most efficient way is to use a single RUN command which contains multiple commands seoerated by **&&**.

3. To run a docker container using specific command, **CMD** is used. Specifying more than one CMD command will allow only the last one to get executed. 

4. **WORKDIR** instruction specifies the working directory of that container. Any command that is executed after WORKDIR will be executed within this working directory.

5. **COPY** instruction is used to copy a complete directory or file from the local machine to the docker container. 