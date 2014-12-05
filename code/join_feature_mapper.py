#!/usr/bin/env python

# Mapper
# Prepend instance lines with feature ID

import sys

len_side = 0
instance_index = 0

for line in sys.stdin:
    line = line.strip()

    tokens = line.split()
    if len(tokens) == 2:
        print line
    if len(tokens) == 13:
        print '%s\t%s' % (tokens[9], line)
