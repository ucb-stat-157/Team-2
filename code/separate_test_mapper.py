#!/usr/bin/env python

import sys, random

for line in sys.stdin:
    line = line.strip()

    tokens = line.split()

    if tokens[0] == 'test':
        print line
