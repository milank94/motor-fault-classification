# Dockerfile

The idea behind this is to have a Docker container, powered by AltaLab, that people can boot up with the proper
requirements to immediately start running and developing.
This also has the benefit of not restricting developers to specific versions of libraries on their local machines.

## Setup

The creation of the Docker container is a two part process.
1) Build the docker image from the Dockerfile. This only needs to be done once unless there are updates that need to be
 added to the image. You can build the image with this interactive script.
Make sure you do this from the project root folder.
```bash
bash docker/build.sh
```
This script builds the docker image.
The `bash` in front of the filename, lets you run the script.
You will be asked to provide a name for the image. It can be anything, such as {project_name}_img
Keep this name as you will need to it run the docker container

2) Create a docker container from the Docker image. For this step, There is a small bash
script that will create a container from the image in the first step.
It will also link to the main altalab folder so that the scripts can be run inside docker.
The script will ask for the docker image name that you specified earlier and a name for the container
```bash
bash docker/run_docker.sh
```

## Notes
The running command runs the container in detach mode, so, it won't put you inside it yet.
Upon successfully creating the container you will see some instructions on how to start and stop the container
Those instructions can be found in the [README](../README.md#Usage)

After creating the container, you likely won't need to do it again until some updates have been issued for the image.

To step into the container, run:
```bash
sudo docker exec -it container_name bash
```

## Jupyter Notebook Integration
The [run_docker.sh](../docker/run_docker.sh) script exposes port 8888 by default. You can add other ports as needed
by modifying that script

## Docker Resources
If you are new to Docker, you can read through a rough introduction
[here](https://github.com/altaml/home/blob/master/docker.md).
Further tutorials can be found online.
Links to good tutorials and descriptions will be added to the above resource.
