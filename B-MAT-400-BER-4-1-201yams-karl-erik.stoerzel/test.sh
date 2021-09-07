#! /bin/bash

./201yams -h > str1
DIFF=$(diff <(cat str1) <(cat test1))
if [ "$DIFF" != "" ]; then
    exit 1
fi

./201yams 0 0 0 0 0 yams_4 > str1
DIFF=$(diff <(cat str1) <(echo "Chances to get a 4 yams: 0.01%"))
if [ "$DIFF" != "" ]; then
   exit 1
fi

./201yams 1 2 3 4 5 four_4 > str1
DIFF=$(diff <(cat str1) <(echo "Chances to get a 4 four-of-a-kind: 1.62%"))
if [ "$DIFF" != "" ]; then
   exit 1
fi

./201yams 2 2 5 4 6 straight_6 > str1
DIFF=$(diff <(cat str1) <(echo "Chances to get a 6 straight: 16.67%"))
if [ "$DIFF" != "" ]; then
   exit 1
fi

./201yams 0 0 0 0 0 full_2_3 > str1
DIFF=$(diff <(cat str1) <(echo "Chances to get a 2 full of 3: 0.13%"))
if [ "$DIFF" != "" ]; then
   exit 1
fi

./201yams 2 3 2 3 2 full_2_3 > str1
DIFF=$(diff <(cat str1) <(echo "Chances to get a 2 full of 3: 100.00%"))
if [ "$DIFF" != "" ]; then
   exit 1
fi
exit 0