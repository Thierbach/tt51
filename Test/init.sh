#!/bin/bash

echo "Build the Docker Image"
docker build --no-cache -t tt51/pruefung.docker .

echo "Push Image to Docker Hub"
docker push tt51/pruefung.docker

echo "Deploy Secrets to Kubernetes"
minikube kubectl -- apply -f S3Secrets.yaml 

echo "Deploy Image to Kubernetes"
minikube kubectl -- apply -f dockerfile.yaml 

echo "Check Kubernetes Deployments"
minikube kubectl -- get deployments
