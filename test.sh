#!/bin/bash
IFSBAK=$IFS
IFS=" "
name=$1
echo $name
out=None
for i in {1..10}
do
echo $i
cat 'D:/SkyDrive/Documents/Università/Fordham/Courses/BigData/Works/Project1/NBA/shot_logs.csv' | python mapper1.py "$name" $i "$out"  | sort -k1,1 | python reducer1.py > output.txt
decision=$(tail -c 3 output.txt)
out=$(cat output.txt)
if (test $decision -eq 1); then 
echo "decision break"
break
fi
echo "decision continue"
echo $out
done

echo 'final zone and correspondent hit rate:'
cat 'D:/SkyDrive/Documents/Università/Fordham/Courses/BigData/Works/Project1/NBA/shot_logs.csv' | python mapper2.py "$name" "$out" | sort -k1,1 | python reducer2.py

IFS=$IFSBAK