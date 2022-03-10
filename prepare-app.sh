#!/bin/bash
echo "Preparing app..."
docker build . -t convert:dev
az group create --name skuska --location eastus
az aks create --resource-group skuska --name skuskacluster --node-count 2 --enable-addons monitoring --generate-ssh-keys
az aks get-credentials --resource-group skuska --name skuskacluster
kubectl create namespace skuska
kubectl apply -f statefulset.yaml -n skuska
kubectl apply -f deployment.yaml -n skuska
kubectl apply -f service.yaml -n skuska
