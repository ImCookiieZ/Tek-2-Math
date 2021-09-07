#! /bin/bash

./205IQ -h > str1
DIFF=$(diff <(cat str1) <(cat test1.txt))
if [ "$DIFF" != "" ]; then
    exit 1
fi

./205IQ 100 15 > str1
DIFF=$(diff <(head -n 2 str1) <(echo "0 0.00000
1 0.00000"))
if [ "$DIFF" != "" ]; then
    exit 1
fi

DIFF=$(diff <(head -n 120 str1 | tail -n 10) <(echo "110 0.02130
111 0.02033
112 0.01931
113 0.01827
114 0.01721
115 0.01613
116 0.01506
117 0.01399
118 0.01295
119 0.01192"))
if [ "$DIFF" != "" ]; then
    exit 1
fi

DIFF=$(diff <(tail -n 2 str1) <(echo "199 0.00000
200 0.00000"))
if [ "$DIFF" != "" ]; then
    exit 1
fi

cd .github
../205IQ 100 24 90 > str1
DIFF=$(diff <(cat str1) <(echo "33.8% of people have an IQ inferior to 90"))
if [ "$DIFF" != "" ]; then
    exit 1
fi

cd ..
./205IQ 100 24 90 95 > str1
DIFF=$(diff <(cat str1) <(echo "7.9% of people have an IQ between 90 and 95"))
if [ "$DIFF" != "" ]; then
    exit 1
fi