#!/usr/bin/env python

# Author: Kevin Shieh

# Mapper
# Maps instance lines to clicks \t impressions \t proportion of
# query tokens contained in feature tokens

import sys

for line in sys.stdin:
    line = line.strip()

    tokens = line.split()

    if len(tokens) == 14:
        query_tokens = tokens[12]
        other_tokens = tokens[13]

        query_tokens = query_tokens.split('|')
        other_tokens = other_tokens.split('|')

        other_tokens = set(other_tokens)

        count = 0
        total = 0
        for query_token in query_tokens:
            if query_token in other_tokens:
                count += 1
            total += 1

        if total != 0:
            prop = float(count) / total
            print '%s\t%s\t%s' % (tokens[0], tokens[1], prop)
