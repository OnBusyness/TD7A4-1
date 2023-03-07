# TD7A4

To start with it, you have to pull mongo and python latest image 

docker pull mongo:latest

docker pull python:latest

Then you can use the following command : 
docker compose version to check if you have docker compose available

We create a network : docker network create --driver bridge mynetworktd6

Then, we create a container with mongo : docker run -d network mynetworktd6 --name mongodb -p 27017 mongo

Then we build a image for the flask app : docker build --tag td6 .
and we start the container : docker run -d --network mynetworktd6 -p 5000:5000 --name mycontainer -v home/aminesrr:/app/data td6
