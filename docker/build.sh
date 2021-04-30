#!/bin/bash

echo "This script will build the Deep Dive docker image for you"

if test $docker_img_name; then
    echo "Building docker image: $docker_img_name"
else
    echo "Please start by entering a name for the docker image for this project"
    echo "Lower case letters with words separated by underscores"
    read -p "Image name = " docker_img_name
fi

echo "The following commands requrie SUDO previledges. Do you wish to proceed?"
select yn in "Yes" "No"; do
    case $yn in
    Yes)
        echo "The first thing it needs to do is grab AltaLab.
        If this runs into an error, please make sure your
        system has ssh access to AltaML's git repos."
        if [ -d "AltaLab" ]; then
            echo "AltaLab already exists"
        else
            git clone git@github.com:altaml/AltaLab.git
        fi
        sudo docker build --rm -t $docker_img_name -f docker/Dockerfile .
        sudo docker images -f reference=$docker_img_name
        echo "Image building done, if you don't need the AltaLab folder, feel free to erase it."
        break
        ;;
    No) exit ;;
    esac
done
