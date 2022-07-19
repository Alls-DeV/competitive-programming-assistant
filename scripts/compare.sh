#!/usr/bin/env bash

RED='\033[1;31m'
PURPLE='\033[1;35m'
NC='\033[0m' # no color

if [ "$1" == "h" ] ; then
    echo -e "${PURPLE}compare.sh  solution1  solution2  generator  numTests${NC}"
	echo ""
	echo -e "${RED}REMOVE //testcase${NC}"
    exit 0
fi
for ((testNum=0;testNum<$4;testNum++))
do
    ./$3 > input
    ./$2 < input > outSlow
    ./$1 < input > outWrong
    H1=`md5sum outWrong`
    H2=`md5sum outSlow`
    if !(cmp -s "outWrong" "outSlow")
    then
        echo -e "${RED}Error found!${NC}"
        echo -e "${PURPLE}Input:${NC}"
        cat input
        echo -e "${PURPLE}$2 output:${NC}"
        cat outWrong
        echo -e "${PURPLE}$3 output:${NC}"
        cat outSlow
        exit
    fi
done
echo Passed $4 tests

