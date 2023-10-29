#!/usr/bin/env python

import sys

# Define a function to check if a given string represents a number.
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Iterate through each line from standard input (sys.stdin)
for line in sys.stdin:
    # Split the line into a list of values using spaces as separators.
    values = line.strip().split()

    for value in values:
        if is_number(value):
            print 'Value\t%s' % value 


