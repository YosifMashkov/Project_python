#!/bin/bash

docker build -t Random_User_Call -f Dockerfile
docker tag Random_User_Call
docker push Random_User_Call