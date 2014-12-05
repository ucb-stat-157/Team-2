#!/usr/bin/env python

# Mapper
# Roughly 0.2 data in validation set, 0.2 in test set, 0.6 in training set

import sys, random

for line in sys.stdin:
    line = line.strip()

    val = random.random()

    if val < 0.2:
        print '%s\t%s' % ('validation', line)
    elif val < 0.4:
        print '%s\t%s' % ('test', line)
    else:
        print '%s\t%s' % ('train', line)
