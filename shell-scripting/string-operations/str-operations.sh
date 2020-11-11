#! /bin/bash

str="This is a string"
echo "String:   ${str}"

#Print length of string
echo "Length of String :    "${#str}


#String Extraction
POS=5
LEN=10
echo "${str:$POS:$LEN}"

#Ommiting LEN will print string end of the length
echo "${str:$POS}"

echo "${str:$LEN}"