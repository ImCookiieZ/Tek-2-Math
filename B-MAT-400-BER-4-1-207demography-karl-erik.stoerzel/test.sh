#! /bin/bash

./207demography EUU > str1
DIFF=$(diff <(cat str1) <(cat solutions/test1))
if [ "$DIFF" != "" ]; then
  echo "$DIFF"
  exit 1
fi
./207demography BRA BOL PER > str1
DIFF=$(diff <(cat str1) <(cat solutions/test2))
if [ "$DIFF" != "" ]; then
  echo "$DIFF"
  exit 1
fi
./207demography BRA EUU GER > str1
DIFF=$(diff <(cat str1) <(cat solutions/test3))
if [ "$DIFF" != "" ]; then
  echo "$DIFF"
  exit 1
fi
./207demography GER AUS BDI ARG > str1
DIFF=$(diff <(cat str1) <(cat solutions/test4))
if [ "$DIFF" != "" ]; then
  echo "$DIFF"
  exit 1
fi

rm str1