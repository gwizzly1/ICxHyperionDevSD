#!/bin/bash

if [ -d "new_folder" ]
then
    mkdir if_folder
    echo "Created 'if_folder'."
else
    echo "'new_folder' does not exist."
fi

if [ -d "if_folder" ]
then
    mkdir hyperionDev
    echo "'hyperionDev' folder created"
else
    mkdir new_projects
    echo "'new_projects' folder created"
fi