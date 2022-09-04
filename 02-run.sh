#!/bin/bash

NAMESPACE="gabepublic"
IMG_NAME="api-countries-pyflask"
APPNAME="api-countries"

BUILD_VER=0.1.0
PLATFORM="linux-amd64"

docker run --rm -d --name $APPNAME -p 80:5000 $NAMESPACE/$IMG_NAME:$BUILD_VER-$PLATFORM
