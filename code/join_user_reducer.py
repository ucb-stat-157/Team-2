#!/usr/bin/env python

# Author: Kevin Shieh

# Reducer
# Join on user ID by appending user age and gender to instance lines
# Assumed that input data is sorted

import sys

current_userid = None
userid = None
training_lines = []
user_tokens = None

for line in sys.stdin:
    line = line.strip()
    tokens = line.split('\t')
    line = line.split('\t', 1)

    userid = line[0]
    if current_userid != userid:
        if len(training_lines) > 0 and user_tokens != None:
            for inst in training_lines:
                print '%s\t%s' % (inst, user_tokens)
            training_lines = []
            user_tokens = None

        if len(tokens) == 3:
            user_tokens = line[1]
        if len(tokens) == 13:
            training_lines.append(line[1])

        current_userid = userid

    else:
        if len(tokens) == 3:
            user_tokens = line[1]
        if len(tokens) == 13:
            training_lines.append(line[1])

for inst in training_lines:
    print '%s\t%s' % (inst, user_tokens)
