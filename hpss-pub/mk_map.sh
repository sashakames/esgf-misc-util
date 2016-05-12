#!/bin/bash

path=`./urlencode.py $1`

project=$2

digest=`./gen_digest.py $path`

url="https://pcmdi11.llnl.gov/basej/metadata?path=$path&digest=$digest"

#echo $url

resp=`curl -s -k $url`

key=`echo $resp | ./parsekey.py`  

#echo $key

exurl="https://pcmdi11.llnl.gov/basej/expose/$2?path=$path&key=$key"

#echo $exurl

#curl -X POST -k $exurl

echo $resp | ./json2map.py $project $project.$3