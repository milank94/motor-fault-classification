#!/bin/bash

# This bash script creates a docker container and runs it
# to train a model. Depending on Config file train is performed
# either on Azure ML cluster or locally. When Training on Azure
# the model and artifact will be logged in the Azure Workspace.

echo "Please enter the name of the docker image that is going to be built for this project"
read -p "Image name = " docker_img_name
echo "Please enter a name for the docker container"
echo "It should be all lower case with underscores between words"
read -p "Container name = " docker_container_name

sudo docker build --rm -t $docker_img_name \
    -f docker/Dockerfile_TrainPipeline .

sudo docker run \
    -it \
    -v $PWD:/src/model \
    -w /src/model \
    --name $docker_container_name \
    $docker_img_name
