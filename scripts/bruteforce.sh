#!/usr/bin/env bash

RED='\033[0;35m'
BLUE='\033[0;36m'
NC='\033[0m' # no color

if [ "$1" == "-h" ] ; then
	echo -e "${RED}EXAMPLE"
	echo "bruteforce.sh  brute  generator  numTests"
	echo ""
	echo -e "${BLUE}remove cin >> testcase${NC}"
    exit 0
fi
for ((testNum=0;testNum<$3;testNum++))
do
	echo -e "${RED}-----------------------------${NC}"
    ./$2.exe > input
	echo -e "${BLUE}Input:${NC}"
    cat input
	echo -e "${BLUE}Output:${NC}"
    ./$1.exe < input
done


