#!/bin/bash

# script to generate mapfiles for publishing 

# arguments <PATH> <PROJECT> <DATASET_ID_SUFFIX> 
# $1 = PATH
# ...

SERVER=""

path=`./urlencode.py $1`

project=$2

digest=`./gen_digest.py $path`

url="https://$SERVER/basej/metadata?path=$path&digest=$digest"

#echo $url

resp=`curl -s -k $url`

key=`echo $resp | ./parsekey.py`  

#echo $key

exurl="https://$SERVER/basej/expose/$2?path=$path&key=$key"

#echo $exurl

#curl -X POST -k $exurl

echo $resp | ./json2map.py $project $project.$3

