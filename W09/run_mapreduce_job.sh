#!/bin/bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-input /mapreduce/test.txt \
-output /mapreduce/outputdemo3 \
-mapper mapper.py \
-reducer reducer.py 

