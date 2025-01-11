import docker


#Docker commands


docker container run -it #start a new container interactively
docker container exec -it # run additional command in the existing container

docker container logs #log information about the container

docker container run -p  80:80#expose the port
docker container port #shows exposed ports

docker container inspect --format #common option for formatting the output of commands


docker network ls #show networks
docker network inspect #inspect a network
docker network create --driver #create a network
docker network connect #attach a netwrok to a container
docker network disconnect #detach a network from a container