#!/usr/bin/env bash

RED='\033[1;31m'
PURPLE='\033[1;35m'
NC='\033[0m' # no color

if [ "$1" == "h" ] ; then
    echo -e "${PURPLE}stress.sh  wrong  slow  generator  numTests${NC}"
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
        echo "${RED}Error found!${NC}"
        echo "${PURPLE}Input:${NC}"
        cat input
        echo "${PURPLE}Wrong Output:${NC}"
        cat outWrong
        echo "${PURPLE}Slow Output:${NC}"
        cat outSlow
        exit
    fi
done
echo Passed $4 tests


