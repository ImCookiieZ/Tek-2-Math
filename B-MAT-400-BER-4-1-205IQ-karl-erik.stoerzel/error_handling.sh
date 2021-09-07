#! /bin/bash

(./205IQ 1 ; echo $?) > str1
DIFF=$(diff <(cat str1) <(echo "84"))
if [ "$DIFF" != "" ]; then
    exit 1
fi

(./205IQ ha; echo $?) > str1
DIFF=$(diff <(cat str1) <(echo "84"))
if [ "$DIFF" != "" ]; then
    exit 1
fi

(./205IQ 3 3 ha; echo $?) > str1
DIFF=$(diff <(cat str1) <(echo "84"))
if [ "$DIFF" != "" ]; then
    exit 1
fi

(./205IQ 3 3 3 2; echo $?) > str1
DIFF=$(diff <(cat str1) <(echo "84"))
if [ "$DIFF" != "" ]; then
    exit 1
fi

(./205IQ 3 3 300; echo $?) > str1
DIFF=$(diff <(cat str1) <(echo "84"))
if [ "$DIFF" != "" ]; then
    exit 1
fi