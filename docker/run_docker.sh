echo "Please enter the name of the docker image that was built for this project"
echo "Hint: it should look like this: project_name_img"
read -p "Image name = " docker_img_name
echo "Please enter a name for the docker container"
echo "It should be all lower case with underscores between words"
read -p "Container name = " docker_container_name
echo "Please enter a port number for jupyter.
Make sure it doesn't conflict with other instances. Here are the taken ports"
printf '\e[1;34m%-6s\e[m' "$(for container in $(docker container ls -a | awk '{print $1}' | tail -n+2);
    do docker inspect \
    --format='{{.Name}} {{range $p, $conf := .HostConfig.PortBindings}} {{$p}} -> {{(index $conf 0).HostPort}} {{end}}'\
    ${container};
done)
"
read -e -i "8888" -p "Your port (Default = 8888) = " port_number

sudo docker run \
    -it \
    -d \
    -p $port_number:8888 \
    -v $PWD:/src/work \
    -w /src/work \
    --env USER=$USER \
    --name $docker_container_name \
    $docker_img_name


echo "To start using this container, as long as it is running, you only need to run this command

    sudo docker exec -it $docker_container_name bash

To start/stop/remove this container:
    sudo docker start $docker_container_name
    sudo docker stop $docker_container_name
    sudo docker rm $docker_container_name"
