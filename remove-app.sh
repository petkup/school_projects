#!/bin/bash
echo "Removing app..."
kubectl delete namespace skuska
kubectl delete pv persistent-volume1
az group delete --name skuska --yes --no-wait
