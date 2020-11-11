#! /bin/bash
#Passing argument through command line 
echo $0 $1 $2 $3    '> echo $1 $2 $3'

args=("$@")

echo ${args[0]} ${args[1]} ${args[2]} ${args[3]}

echo "Length of array:      "$#
echo "Print Arry Elements:   "  $@