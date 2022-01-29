# Base Image
FROM node:13-slim

# Folder on the container where we will place our files 
WORKDIR /app

# Add all of the files from this folder to the app folder
ADD . /app 

# The command that you want the container to start with 
CMD node server.js

# To build the docker container 
    # docker build -t cloudrunapp . 

# To run the docker container 
    # docker run -it -p 8080:8080 cloudrunapp

    
