#!/usr/bin/env python

# Author: Kevin Shieh

# Mapper
# Run through a EMR job to separate test data into individual directory

import sys, random

for line in sys.stdin:
    line = line.strip()

    tokens = line.split()

    if tokens[0] == 'test':
        print line
