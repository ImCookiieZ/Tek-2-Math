  
#! /bin/bash

(./207demography 1 ; echo $?) > str1
DIFF=$(diff <(cat str1) <(echo "84"))
if [ "$DIFF" != "" ]; then
    exit 1
fi

(./207demography ha; echo $?) > str1
DIFF=$(diff <(cat str1) <(echo "84"))
if [ "$DIFF" != "" ]; then
    exit 1
fi

(./207demography -l ha; echo $?) > str1
DIFF=$(diff <(cat str1) <(echo "84"))
if [ "$DIFF" != "" ]; then
    exit 1
fi

(./207demography GER -h ARG; echo $?) > str1
DIFF=$(diff <(cat str1) <(echo "84"))
if [ "$DIFF" != "" ]; then
    exit 1
fi