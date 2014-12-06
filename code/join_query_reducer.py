#!/usr/bin/env python

# Author: Kevin Shieh

# Reducer
# Join on queryID by appending query tokens to instance lines
# Assumed that input data is sorted

import sys

current_id = None
query_id = None
lines = []
query_tokens = None

for line in sys.stdin:
    line = line.strip()
    tokens = line.split('\t')
    line = line.split('\t', 1)

    query_id = line[0]
    if current_id != query_id:
        if len(lines) > 0 and query_tokens != None:
            for inst in lines:
                print '%s\t%s' % (inst, query_tokens)
            lines = []
            query_tokens = None

        if len(tokens) == 2:
            query_tokens = line[1]
        if len(tokens) == 13:
            lines.append(line[1])

        current_id = query_id

    else:
        if len(tokens) == 2:
            query_tokens = line[1]
        if len(tokens) == 13:
            lines.append(line[1])
