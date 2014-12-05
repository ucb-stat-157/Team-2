#!/usr/bin/env python

# Mapper
# Prepend instance lines with queryID

import sys

for line in sys.stdin:
    line = line.strip()

    tokens = line.split('\t')
    if len(tokens) == 2:
        print line
    if len(tokens) == 12:
        print '%s\t%s' % (tokens[7], line)
