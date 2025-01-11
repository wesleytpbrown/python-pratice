import docker


#Docker commands


docker container run -it #start a new container interactively
docker container exec -it # run additional command in the existing container

docker container logs #log information about the container

docker container run -p  80:80#expose the port


