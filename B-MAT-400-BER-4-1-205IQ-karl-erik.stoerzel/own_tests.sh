#! /bin/bash

./205IQ 50 62 > str1
DIFF=$(diff <(str1 | cut -f2 -d" ") <(cat my_results1.txt))
if [ "$DIFF" != "" ]; then
    exit 1
fi


cd .github
../205IQ 34 98 73 > ../str1
DIFF=$(diff <(cat ../str1) <(echo "29.0% of people have an IQ inferior to 73"))
if [ "$DIFF" != "" ]; then
    exit 1
fi

cd ..
./205IQ 83 92 89 99 > str1
DIFF=$(diff <(cat str1) <(echo "4.3% of people have an IQ between 89 and 99"))
if [ "$DIFF" != "" ]; then
    exit 1
fi