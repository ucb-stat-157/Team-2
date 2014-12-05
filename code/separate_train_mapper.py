#!/usr/bin/env python

# Mapper
# Run through a EMR job to separate train data into individual directory

import sys, random

for line in sys.stdin:
    line = line.strip()

    tokens = line.split()

    if tokens[0] == 'train':
        print line
