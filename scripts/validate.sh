#!/usr/bin/env bash

RED='\033[0;35m'
BLUE='\033[0;36m'
NC='\033[0m' # no color

if [ "$1" == "-h" ] ; then
	echo -e "${RED}EXAMPLE"
	echo "validate.sh  solution  validator  generator  numTests"
	echo ""
	echo -e "${BLUE}remove cin >> testcase"
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
        echo -e "${BLUE}Input:${NC}"
        cat input
        echo -e "${BLUE}Output:${NC}"
        cat out
        echo -e "${BLUE}Validator result:${NC}"
        cat res 
        exit
    fi
done
echo Passed $4 tests


