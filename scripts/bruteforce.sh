#!/usr/bin/env bash

RED='\033[1;31m'
PURPLE='\033[1;35m'
NC='\033[0m' # no color

if [ "$1" == "h" ] ; then
	echo -e "${PURPLE}bruteforce.sh  brute  generator  numTests${NC}"
	echo ""
	echo -e "${RED}REMOVE //testcase${NC}"
    exit 0
fi
for ((testNum=0;testNum<$3;testNum++))
do
	echo -e "${RED}-----------------------------${NC}"
    ./$2 > input
    cat input
    ./$1 < input
	
done


