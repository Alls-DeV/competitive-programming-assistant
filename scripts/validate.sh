#!/usr/bin/env bash

if [ "$1" == "-h" ] ; then
	echo "validate.sh  wrong  validator  generator  numTests"
	echo ""
	echo "remove //testcase from generator and validator"
	echo "validator should return "OK" or the string that explain the error"
	echo "validator first take in input the generator input and next the program output"
    exit 0
fi
for ((testNum=0;testNum<$4;testNum++))
do
    ./$3 > input
    ./$1 < input > out
    cat input out > data
    ./$2 < data > res
    result=$(cat res)
    if [ "${result:0:2}" != "OK" ];
    then
        echo "Error found!"
        echo "Input:"
        cat input
        echo "Output:"
        cat out
        echo "Validator Result:"
        cat res 
        exit
    fi
done
echo Passed $4 tests


