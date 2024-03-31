#!/bin/bash

# Configure the following values
RAPIDJSON_FOLDER=./rapidjson
NS3_FOLDER=./ns-allinone-3.41/ns-3.41
#NS3_FOLDER=./ns-allinone-3.41/ns-3.41

# Do not change
mkdir -p $NS3_FOLDER/rapidjson
cp  -r $RAPIDJSON_FOLDER/include/rapidjson/* $NS3_FOLDER/rapidjson/
cp src/applications/model/* $NS3_FOLDER/src/applications/model/
cp src/applications/helper/* $NS3_FOLDER/src/applications/helper/
cp src/internet/helper/* $NS3_FOLDER/src/internet/helper/
cp scratch/* $NS3_FOLDER/scratch/
