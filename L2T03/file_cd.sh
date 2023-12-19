#!/bin/bash

# This is to create 3 folders, enter a folder and create 3 more folders inside, then remove 2
mkdir folder_1 folder_2 folder_3
echo "3 folders created"
cd folder_1
echo "Entered folder_1"
mkdir folder_1_1 folder_1_2 folder_1_3
echo "Created 3 folders within folder_1"
rmdir folder_1_3 folder_1_2
echo "Removed 2 folders within folder_1"