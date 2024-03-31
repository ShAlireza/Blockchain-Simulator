#!/bin/bash

source venv2.7/bin/activate
cd ns-allinone-3.25/ns-3.25

./waf --run "scratch/double-spend --ud=1 --iterations=$1 --q=$2 --z=$3 --noBlocks=$4"