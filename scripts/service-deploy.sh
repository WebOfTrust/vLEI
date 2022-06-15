#!/bin/bash

KUBE_CONFIG=~/.gleif/kubeconfig.yaml

if [[ ! -f $KUBE_CONFIG ]] ; then
    echo "kube config file "${KUBE_CONFIG}" must exist."
    echo "exiting"
    exit
fi

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

helm install vlei-server-service ./services -f ${SCRIPT_DIR}/gleif-vlei-values.yaml --kubeconfig ${KUBE_CONFIG} --namespace=gleif-vlei-server-pilot --create-namespace

