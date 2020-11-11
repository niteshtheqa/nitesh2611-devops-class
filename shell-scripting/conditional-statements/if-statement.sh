#! /bin/bash


count=10
if [ $count -eq 10 ]
then
    echo 'condition is true'
fi

echo "Checking string validation...."

word="nitesh"
if [ $word == "nitesh" ]
then
    echo "Condition is true"
else
    echo "Condition is false"
fi
