#!/usr/bin/env python

# Mapper
# Keep relevant info

import sys

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()

    # tokens[3] = rate
    # tokens[0] = type (train, test, validation)
    # tokens[1] = clicks
    # tokens[3] = impressions
    print '%s\t%s\t%s\t%s' % (tokens[3], tokens[0], tokens[1], tokens[2])
