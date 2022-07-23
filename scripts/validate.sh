#!/usr/bin/env bash

RED='\033[1;31m'
PURPLE='\033[1;35m'
NC='\033[0m' # no color

if [ "$1" == "h" ] ; then
	echo -e "${PURPLE}validate.sh  solution  validator  generator  numTests${NC}"
	echo ""
	echo -e "${RED}REMOVE //testcase"
	echo "validator should return "OK" or the string that explain the error"
	echo -e "validator first take in input the generator input and next the program output${NC}"
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
        echo -e "${RED}Error found!${NC}"
        echo -e "${PURPLE}Input:${NC}"
        cat input
        echo -e "${PURPLE}Output:${NC}"
        cat out
        echo -e "${PURPLE}Validator result:${NC}"
        cat res 
        exit
    fi
done
echo Passed $4 tests


