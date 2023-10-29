#!/usr/bin/env python


from operator import itemgetter
import sys

total = 0
count = 0

# Iterate through each line from standard input (sys.stdin).
for line in sys.stdin:
    try:
        # Split each line into a key and value using the tab character as a separator.
        key, value = line.strip().split('\t')
        if key == "Value":
            total += float(value)
            count += 1
    except ValueError:
        continue

if count > 0:
    average = total / count
    print 'AVERAGE=%s' % average

